from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, roles_required, db, os
from iomate.models import Esxis, Servers, VirtualMachines, Saltstack_pxe_nodes, Customer_sw, Switch1_24_port, Switch1_48_port, Switch2_24_port, Switch2_48_port
#import xmlrpclib
#from xmlrpclib import *
import cobbler.api as capi
import re

system_profiles = Blueprint('system_profiles', __name__)

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

### SYSTEM-PROFILES ###
@system_profiles.route('/system-profiles', methods=['GET', 'POST'])
@login_required
def system_profiles_view():
    error = None
    if request.method == 'GET':
	napalm_switch1_macs = napalm_switch_mac_audit(1)
        list_of_profiles = cobbler_server.profiles()
        systems = cobbler_server.systems()
        return render_template('system-profiles.html', napalm_switch1_macs=napalm_switch1_macs, list_of_profiles=list_of_profiles, systems=systems, servers=Servers.query.all(), esxis=Esxis.query.all(), virtualmachines=VirtualMachines.query.all(), salt_pxe_nodes=Saltstack_pxe_nodes.query.all())
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
                    find_vm = VirtualMachines.query.filter_by(hostname=system_name).first()
		    if str(find_esxi) == str(system_name):
                        find_host = find_esxi
			intname = "vmnic0"
		    elif str(find_server) == str(system_name):
		        find_host = find_server
                        intname = "ens192"
		    elif str(find_vm) == str(system_name):
		        find_host = find_vm
                        intname = "ens160"
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
                    flash('System Profile ' + system_name + ' Saved','success')
                    return redirect(request.url)
        if 'cobbler_system_delete' in request.form:
            if not request.form['cobbler_system_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Form Error</div>"
            else:
                system_name = request.form.get('id')
	        print system_name
#                system_name = request.form['system_name']
                cobbler_server.remove_system(system_name)
                os.system("service cobblerd restart")
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Cobbler System Deleted</div>"
#                flash('Template generated successfully !','success')
#                return redirect(request.url)
        else:
            flash('Malformed form submitted !','danger')
            return redirect(request.url)

