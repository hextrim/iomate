from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, roles_required, db, os
from iomate.models import VirtualMachines, Saltstack_pxe_nodes, Customer_sw, Switch1_24_port, Switch1_48_port, Switch2_24_port, Switch2_48_port, System_vm_profiles, System_phy_profiles
import xmlrpclib
from xmlrpclib import *
import cobbler.api as capi
import re
import time

system_vm_profiles = Blueprint('system_vm_profiles', __name__)

### LOCAL CONFIG ###
cobbler_server = capi.BootAPI(is_cobblerd=True)
cobbler_server_xmlrpc = xmlrpclib.Server("http://192.168.1.83/cobbler_api")
token = cobbler_server_xmlrpc.login("cobbler", "cobbler")

### SYSTEM-PROFILES ###
@system_vm_profiles.route('/system-vm-profiles', methods=['GET', 'POST'])
@login_required
def system_vm_profiles_view():
    error = None
    if request.method == 'GET':
        list_of_profiles = cobbler_server.profiles()
        systems = cobbler_server_xmlrpc.get_systems()
#        systems = cobbler_server.systems()
        return render_template('system-vm-profiles.html', list_of_profiles=list_of_profiles, systems=systems, virtualmachines=VirtualMachines.query.all(), salt_pxe_nodes=Saltstack_pxe_nodes.query.all())
    elif request.method == 'POST':
        if 'system_profiles_save' in request.form:
            if not request.form['system_name'] or not request.form['system_switch_port_mac'] or not request.form['system_salt_pxe_node'] or not request.form['system_profile']:
                flash('Please fill all fields before sending a request !','danger')
                return redirect(request.url)
            else:
                if re.sub(r"^.*=","", request.form['system_switch_port_mac']).lower() != request.form['system_salt_pxe_node']:
                    flash('Switch Port MAC does not match PXE booted SALT agent !','danger')
                    return redirect(request.url)
                else:
		    system_name = request.form['system_name']
                    find_vm = VirtualMachines.query.filter_by(hostname=system_name).first()
		    if str(find_vm) == str(system_name):
		        find_host = find_vm
                        intname = "ens160"
		    else:
			find_host = 'NOT FOUND'
		    system_switch_port_mac = re.sub(r"^.*=","", request.form['system_switch_port_mac']).lower()
		    system_salt_pxe_node = request.form['system_salt_pxe_node']
		    system_profile = request.form['system_profile']
#                   intname = "vmnic0"
                    system = cobbler_server.new_system()
                    system.name = system_name
	 	    system.profile = system_profile
                    system.set_hostname(find_host.hostname)
		    system.set_name_servers("8.8.8.8")
		    system.set_static(True, intname)
		    system.set_mac_address(system_switch_port_mac, intname)
		    system.set_ip_address(find_host.ipaddress, intname)
		    system.set_netmask(find_host.subnet, intname)
		    system.set_if_gateway(find_host.gateway, intname)
                    system.set_gateway(find_host.gateway)
		    cobbler_server.systems().add(system,with_copy=True)
                    cobbler_server.add_system(system, save=True)
		    os.system("service cobblerd restart") 
                    time.sleep(2)
                    system_vm_profile_check = System_vm_profiles.query.filter_by(name=system_name).first()
		    if str(system_vm_profile_check) == str(system_name):
                        salt_pxe_node = Saltstack_pxe_nodes.query.filter_by(pxemac=system_salt_pxe_node).one()
                        salt_pxe_node.pxeinstalled = False
                        db.session.add(salt_pxe_node)
#                        db.session.commit()
                        system_vm_profile = System_vm_profiles.query.filter_by(mac=system_switch_port_mac).one()
                        salt_pxe_node = Saltstack_pxe_nodes.query.filter_by(pxemac=system_salt_pxe_node).one()
                        salt_pxe_node.saltvmbackref = system_vm_profile
                        db.session.commit()
                        flash('This System already exist. System OS updated and System Network Enabled !','success')
                        return redirect(request.url)
                    else:
                        system_vm_profiles = System_vm_profiles(system_name, system_salt_pxe_node)
                        db.session.add(system_vm_profiles)
		        system_vm_profile = System_vm_profiles.query.filter_by(mac=system_switch_port_mac).one()
		        salt_pxe_node = Saltstack_pxe_nodes.query.filter_by(pxemac=system_salt_pxe_node).one()
		        salt_pxe_node.saltvmbackref = system_vm_profile
#                    db.session.add(system_vm_profile)
                        db.session.add(salt_pxe_node)
                        db.session.commit()
                        flash('System Profile ' + system_name + ' Saved','success')
                        return redirect(request.url)
        if 'system_vm_edit' in request.form:
            if not request.form['id'] or not request.form['system_profile'] or not request.form['system_netboot_enabled']:
                flash('Please fill all fields before sending a request !','danger')
                return redirect(request.url)
            else:
                system_name = request.form.get('id')
                system_profile = request.form['system_profile']
                system_netboot_enabled = request.form['system_netboot_enabled']
                system = cobbler_server.find_system(system_name)
                system.name = system_name
                system.profile = system_profile
		system.netboot_enabled = system_netboot_enabled
                cobbler_server.systems().add(system,with_copy=True)
                cobbler_server.add_system(system, save=True)
                os.system("service cobblerd restart")
                time.sleep(2)
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Cobbler System Edited</div>"
        if 'system_vm_delete' in request.form:
            if not request.form['system_vm_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Form Error</div>"
            else:
                system_name = request.form.getlist('id')
                for system in system_name:
                    system_phy_profiles = System_phy_profiles.query.filter_by(name=system).first()
                    system_vm_profiles = System_vm_profiles.query.filter_by(name=system).first()
                    if str(system_phy_profiles) == str(system):
                        cobbler_server.remove_system(system)
                        system_vm_profiles = System_phy_profiles.query.filter_by(name=system).first()
                        db.session.delete(system_phy_profiles)
                        db.session.commit()
                    elif str(system_vm_profiles) == str(system):
                        cobbler_server.remove_system(system)
                        system_vm_profiles = System_vm_profiles.query.filter_by(name=system).first()
                        db.session.delete(system_vm_profiles)
                        db.session.commit()
                    else:
                        return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Cobbler System ERROR</div>"
                os.system("service cobblerd restart")
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Cobbler System Deleted</div>"
#                for system in system_name:
#                    cobbler_server.remove_system(system)
#                    system_vm_profiles = System_vm_profiles.query.filter_by(name=system).first()
#                    db.session.delete(system_vm_profiles)
#                    db.session.commit()
#	        os.system("service cobblerd restart")
#                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Cobbler System Deleted</div>"
        else:
            flash('Malformed form submitted !','danger')
            return redirect(request.url)
