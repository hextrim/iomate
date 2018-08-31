#from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException

# import NAPALM Base
#import napalm.base.helpers
#from napalm.base import NetworkDriver
#from napalm.base.utils import py23_compat
##from napalm.base.exceptions import ConnectionException
#from napalm.base.exceptions import CommandErrorException
#import napalm.base.constants as c


from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, roles_required, db, os
from iomate.models import Esxis, Servers, Saltstack_pxe_nodes, Customer_sw, Switch1_24_port, Switch1_48_port, Switch2_24_port, Switch2_48_port, System_phy_profiles, System_vm_profiles
#import xmlrpclib
#from xmlrpclib import *
import cobbler.api as capi
import re
import time

system_phy_profiles = Blueprint('system_phy_profiles', __name__)

### LOCAL CONFIG ###
# Custom filter method
#def regex_replace(s, find, replace):
#    """A non-optimal implementation of a regex filter"""
#    return re.sub(find, replace, s)
#
#jinja_environment.filters['regex_replace'] = regex_replace

cobbler_server = capi.BootAPI(is_cobblerd=True)
#cobbler_server = xmlrpclib.Server("http://192.168.1.83/cobbler_api")
#token = cobbler_server.login("cobbler", "cobbler")

### NAPALM ###
import napalm
from napalm import get_network_driver
def napalm_switch_mac_audit(customer_sw_id):
    driver = get_network_driver('ios')
    optional_args = {'secret': ''}
## query customer_sw1 for ip_address and nr of switch ports, and port type
    customer_sw = Customer_sw.query.filter_by(id=customer_sw_id).one()
    customer_sw_number_of_ports = customer_sw.customerswbackref.portnr
    customer_sw_port_type = customer_sw.customerswbackref.porttype
    customer_sw_ip_address = customer_sw.customerswbackref.ipaddress
    print customer_sw
    print customer_sw_id
    print customer_sw_number_of_ports
    print customer_sw_port_type
    print customer_sw_ip_address
    if str(customer_sw_id) == '1' and customer_sw_number_of_ports == '24':
        find_pxe_boot_ports = Switch1_24_port.query.filter_by(portpxeboot=True).all()
    elif str(customer_sw_id) == '1' and customer_sw_number_of_ports == '48':
        find_pxe_boot_ports = Switch1_48_port.query.filter_by(portpxeboot=True).all()
    elif str(customer_sw_id) == '2' and customer_sw_number_of_ports == '24':
        find_pxe_boot_ports = Switch2_24_port.query.filter_by(portpxeboot=True).all()
    elif str(customer_sw_id) == '2' and customer_sw_number_of_ports == '48':
        find_pxe_boot_ports = Switch2_48_port.query.filter_by(portpxeboot=True).all()
    else:
        find_pxe_boot_ports = 'DUPA'
## query customer_sw1 for ip_address and nr of switch ports, and port type
    try:
        device = driver(customer_sw_ip_address, 'rancid', '', '280', optional_args=optional_args)
        device.open()
        mac_audit_sw = device.get_mac_address_table()
        pxe_port_mac = []
        for i, item in enumerate(find_pxe_boot_ports):
            if str(customer_sw_port_type) == 'Gi':
                find_mac = filter(lambda x : x['interface'] == 'Gi1/0/' + str(item), mac_audit_sw)
            elif str(customer_sw_port_type) == 'Fa':
                find_mac = filter(lambda x : x['interface'] == 'Fa0/' + str(item), mac_audit_sw)
            if find_mac:
                print (find_pxe_boot_ports[i].devicename + '=' + find_mac[0]['mac'])
	        pxe_port_mac.append(find_pxe_boot_ports[i].devicename + '=' + find_mac[0]['mac'].lower())
            else:
                print (find_pxe_boot_ports[i].devicename + '=None')
                pxe_port_mac.append(find_pxe_boot_ports[i].devicename + '=None')
        print '###'
        print pxe_port_mac
        return pxe_port_mac
    except NetMikoTimeoutException as napalm_error:
        print napalm_error
        return napalm_error

### SYSTEM-PROFILES ###
@system_phy_profiles.route('/system-phy-profiles', methods=['GET', 'POST'])
@login_required
def system_phy_profiles_view():
    error = None
    if request.method == 'GET':
	napalm_switch1_macs = napalm_switch_mac_audit(1)
        list_of_profiles = cobbler_server.profiles()
        systems = cobbler_server.systems()
        return render_template('system-phy-profiles.html', napalm_switch1_macs=napalm_switch1_macs, list_of_profiles=list_of_profiles, systems=systems, servers=Servers.query.all(), esxis=Esxis.query.all(), salt_pxe_nodes=Saltstack_pxe_nodes.query.all())
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
                    find_esxi = Esxis.query.filter_by(hostname=system_name).first()
		    find_server = Servers.query.filter_by(hostname=system_name).first()
		    if str(find_esxi) == str(system_name):
                        find_host = find_esxi
			intname = "vmnic0"
		    elif str(find_server) == str(system_name):
		        find_host = find_server
                        intname = "ens192"
		    else:
			find_host = 'NOT FOUND'
#		    request.form['system_switch_port_mac']
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
                    system_phy_profile_check = System_phy_profiles.query.filter_by(name=system_name).first()
                    if str(system_phy_profile_check) == str(system_name):
                        salt_pxe_node = Saltstack_pxe_nodes.query.filter_by(pxemac=system_salt_pxe_node).one()
                        salt_pxe_node.pxeinstalled = False
                        db.session.add(salt_pxe_node)
#                        db.session.commit()
                        system_phy_profile = System_phy_profiles.query.filter_by(mac=system_switch_port_mac).one()
                        salt_pxe_node = Saltstack_pxe_nodes.query.filter_by(pxemac=system_salt_pxe_node).one()
                        salt_pxe_node.saltvmbackref = system_phy_profile
                        db.session.commit()
                        flash('This System already exist. System OS updated and System Network Enabled !','success')
                        return redirect(request.url)
                    else:
                        system_phy_profiles = System_phy_profiles(system_name, system_salt_pxe_node)
                        db.session.add(system_phy_profiles)
                        system_phy_profile = System_phy_profiles.query.filter_by(mac=system_switch_port_mac).one()
                        salt_pxe_node = Saltstack_pxe_nodes.query.filter_by(pxemac=system_salt_pxe_node).one()
                        salt_pxe_node.saltvmbackref = system_phy_profile
#                    db.session.add(system_vm_profile)
                        db.session.add(salt_pxe_node)
                        db.session.commit()
                        flash('System Profile ' + system_name + ' Saved','success')
                        return redirect(request.url)

#                    system_phy_profiles = System_phy_profiles(system_name, system_salt_pxe_node)
#                    db.session.add(system_phy_profiles)
#                    db.session.commit()
#                    flash('System PHY Profile ' + system_name + ' Saved','success')
#                    return redirect(request.url)
        if 'system_phy_edit' in request.form:
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
        if 'system_phy_delete' in request.form:
            if not request.form['system_phy_delete']:
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
        else:
            flash('Malformed form submitted !','danger')
            return redirect(request.url)

