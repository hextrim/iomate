#from jinja2 import Environment, FileSystemLoader
import jenkins
import codecs
import salt.client
import salt.config
import salt.wheel

from iomate.saltstack import wheel, local
from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db, os, roles_required
from iomate.models import System_vm_profiles, Saltstack_pxe_nodes

##IMPORT FROM IOMATE GLOBAL##
#from iomate.iomate_global import srvjenkins
#from iomate.iomate_global import get_deploy_device_last_build_log
#from iomate.iomate_global import get_deploy_device_get_job_info

deploy_vm_system = Blueprint('deploy_vm_system', __name__)

### LOCAL CONFIG ###
#opts = salt.config.master_config('/etc/salt/master')
#wheel = salt.wheel.WheelClient(opts)
#local = salt.client.LocalClient()

@deploy_vm_system.route("/deploy-vm-system", methods=['GET', 'POST'])
@login_required
#@roles_required('admin')
def deploy_vm_system_view():
    error = None
    if request.method == 'GET':
#        socketio.start_background_task(cct_swx, '/dev/ttyUSB0', 'sw1usbsignal', 'sw1portsignal')
#        socketio.start_background_task(cct_swx, '/dev/ttyUSB1', 'sw2usbsignal', 'sw2portsignal')
#        deploy_sw_1_baseconfig = get_deploy_device_last_build_log('deploy_sw_1_baseconfig')
#        deploy_sw_1_baseconfig_job_info = get_deploy_device_get_job_info('deploy_sw_1_baseconfig')
#        deploy_sw_1_portconfig = get_deploy_device_last_build_log('deploy_sw_1_portconfig')
#        deploy_sw_1_portconfig_job_info = get_deploy_device_get_job_info('deploy_sw_1_portconfig')
#        deploy_sw_1_singleport = get_deploy_device_last_build_log('deploy_sw_1_singleport')
#        deploy_sw_1_singleport_job_info = get_deploy_device_get_job_info('deploy_sw_1_singleport')
        return render_template('deploy-vm-system.html', deploy_vm_systems=System_vm_profiles.query.all(), salt_pxe_nodes=Saltstack_pxe_nodes.query.all())
    elif request.method == 'POST':
        if 'deploy_vm_system' in request.form:
            if not request.form['id']:
                flash('Please fill all the fields before sending a request!','danger')
                return redirect(request.url)
            else:
                deploy_vm_system = request.form.getlist('id')
                for deploy in deploy_vm_system:
		    reboot_vm_system = Saltstack_pxe_nodes.query.filter_by(pxemac=deploy).one()
	            reboot_vm_system_ip = reboot_vm_system.pxeipaddr
                    reboot_vm_system_send_cmd = local.cmd(reboot_vm_system_ip, 'cmd.run', ['shutdown -r now'])
#		    reboot_vm_system.pxeinstalled = True
		    db.session.delete(reboot_vm_system)
		    db.session.commit()
                    wheel.cmd_async({'fun': 'key.delete', 'match': reboot_vm_system_ip })
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>System Rebooted for PXE Installation.</div>"
        else:
            flash('Malformed form submitted !','danger')
            return redirect(request.url)
