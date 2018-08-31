from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, roles_required, db, os
from iomate.models import Saltstack_pxe_nodes
import salt.config
import salt.wheel
import salt.client

saltstack = Blueprint('saltstack', __name__)

### LOCAL CONFIG ###
opts = salt.config.master_config('/etc/salt/master')
wheel = salt.wheel.WheelClient(opts)
local = salt.client.LocalClient()

def salt_service_check():
    PATH='/var/run/salt-master.pid'
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        return "RUNNING"
    else:
	return "STOPPED"

def salt_keys_accepted():
    ret_acc = wheel.cmd('key.list', ['accepted'])
#    return ret_acc['minions']
    return ret_acc

def salt_keys_unaccepted():
    ret_unacc = wheel.cmd('key.list', ['unaccepted'])
#    return ret_unacc['minions_pre']
    return ret_unacc

def salt_keys_denied():
    ret_denied = wheel.cmd('key.list', ['denied'])
    return ret_denied

def salt_keys_rejected():
    ret_rej = wheel.cmd('key.list', ['rejected'])
    return ret_rej


### SALTSTACK ###
@saltstack.route('/saltstack', methods=['GET', 'POST'])
@login_required
def saltstack_view():
    error = None
    if request.method == 'GET':
	salt_svc_check = salt_service_check()
        salt_keys_acc = salt_keys_accepted()
        salt_keys_unacc = salt_keys_unaccepted()
        salt_keys_den = salt_keys_denied()
        salt_keys_rej = salt_keys_rejected()
        return render_template('saltstack.html', pxe_nodes=Saltstack_pxe_nodes.query.all(), salt_svc_check=salt_svc_check, salt_keys_acc=salt_keys_acc, salt_keys_unacc=salt_keys_unacc, salt_keys_den=salt_keys_den, salt_keys_rej=salt_keys_rej)
    elif request.method == 'POST':
        if 'salt_keys_denied_delete' in request.form:
            if not request.form['salt_keys_denied_delete'] or request.form['key_ip'] == '':
                flash('Please fill all the fields before sending a request!','danger')
                return redirect(request.url)
            else:
                key_ip = request.form['key_ip']
		wheel.cmd_async({'fun': 'key.delete', 'match': key_ip })
                pxe_node = Saltstack_pxe_nodes.query.filter_by(pxeipaddr=key_ip).first()
                if str(key_ip) == str(pxe_node):
                    db.session.delete(pxe_node)
                    db.session.commit()
                flash('Requested key ' + key_ip + ' has been removed!','success')
                return redirect(request.url)
        elif 'salt_keys_rejected_delete' in request.form:
            if not request.form['salt_keys_rejected_delete'] or request.form['key_ip'] == '':
                flash('Please fill all the fields before sending a request!','danger')
                return redirect(request.url)
            else:
                key_ip = request.form['key_ip']
                wheel.cmd_async({'fun': 'key.delete', 'match': key_ip })
                pxe_node = Saltstack_pxe_nodes.query.filter_by(pxeipaddr=key_ip).first()
                if str(key_ip) == str(pxe_node):
                    db.session.delete(pxe_node)
                    db.session.commit()
                flash('Requested key ' + key_ip + ' has been removed!','success')
                return redirect(request.url)
        elif 'salt_keys_unaccepted_accept' in request.form:
            if not request.form['salt_keys_unaccepted_accept'] or request.form['key_ip'] == '':
                flash('Please fill all the fields before sending a request!','danger')
                return redirect(request.url)
            else:
                key_ip = request.form['key_ip']
		wheel.cmd('key.accept', [ key_ip ])
                flash('Requested key ' + key_ip + ' has been accepted!','success')
                return redirect(request.url)
        elif 'salt_keys_unaccepted_delete' in request.form:
            if not request.form['salt_keys_unaccepted_delete'] or request.form['key_ip'] == '':
                flash('Please fill all the fields before sending a request!','danger')
                return redirect(request.url)
            else:
                key_ip = request.form['key_ip']
                wheel.cmd_async({'fun': 'key.delete', 'match': key_ip })
                pxe_node = Saltstack_pxe_nodes.query.filter_by(pxeipaddr=key_ip).first()
                if str(key_ip) == str(pxe_node):
                    db.session.delete(pxe_node)
                    db.session.commit()
                flash('Requested key ' + key_ip + ' has been removed!','success')
                return redirect(request.url)
        elif 'salt_keys_accepted_delete' in request.form:
            if not request.form['salt_keys_accepted_delete'] or request.form['key_ip'] == '':
                flash('Please fill all the fields before sending a request!','danger')
                return redirect(request.url)
            else:
                key_ip = request.form['key_ip']
                wheel.cmd_async({'fun': 'key.delete', 'match': key_ip })
                pxe_node = Saltstack_pxe_nodes.query.filter_by(pxeipaddr=key_ip).first()
                if str(key_ip) == str(pxe_node):
                    db.session.delete(pxe_node)
                    db.session.commit()
                flash('Requested key ' + key_ip + ' has been removed!','success')
                return redirect(request.url)
        elif 'salt_keys_audit_save' in request.form:
            if not request.form['salt_keys_audit_save'] or request.form['key_ip'] == '':
                flash('Please fill all the fields before sending a request!','danger')
                return redirect(request.url)
            else:
                key_ip = request.form['key_ip']
		pxe_node_check = Saltstack_pxe_nodes.query.filter_by(pxeipaddr=key_ip).first()
                if str(key_ip) == str(pxe_node_check):
                    flash('Candidate ' + key_ip + ' has already been audited !','danger')
                    return redirect(request.url)
                else:
		    pxe_int_name = local.cmd(key_ip, 'network.ifacestartswith', [ key_ip ])
		    pxe_mac_addr = local.cmd(key_ip, 'network.hwaddr', [ pxe_int_name[key_ip][0] ])
                    pxe_node = Saltstack_pxe_nodes(key_ip, pxe_int_name[key_ip][0], pxe_mac_addr[key_ip])
                    db.session.add(pxe_node)
                    db.session.commit()
#		print pxe_int_name[key_ip][0], pxe_mac_addr[key_ip]
                    flash('Requested key ' + key_ip + ' has been audited! INT: ' + pxe_int_name[key_ip][0] + ' MAC: ' + pxe_mac_addr[key_ip] + ' ','success')
                    return redirect(request.url)
	else:
            flash('Malformed form submitted !','danger')
            return redirect(request.url)

