from jinja2 import Environment, FileSystemLoader
from distutils.util import strtobool
from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db, os
from iomate.models import Switches, Firewalls, Esxis, Servers, Dedicatedsan, Vlans, Switch1_24_port, Customer_sw

design_sw1_24 = Blueprint('design_sw1_24', __name__)

### LOCAL CONFIG ###
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = 'templates/configuration_templates/pyserial'
TEMPLATE_CONFIG = os.path.join(BASE_DIR, TEMPLATE_DIR)

### DESIGN_SW1_24_port ###
@design_sw1_24.route("/design-sw1-24", methods=['GET', 'POST'])
@login_required
def design_switch1_24_port_view():
    error = None
    if request.method == 'GET':
        file = open("output/customer-sw-1-24-portconfig.deploy", "r")
        lines = file.readlines()
        return render_template('design-sw1-24.html', customer_sws=Customer_sw.query.all(), sws=Switches.query.all(), fws=Firewalls.query.all(), esxis=Esxis.query.all(), servers=Servers.query.all(), dedicatedsans=Dedicatedsan.query.all(), vlans=Vlans.query.all(), switch1_24_ports=Switch1_24_port.query.all(), lines=lines)
    elif request.method == 'POST':
        if 'port_config_switch1_24_port_save' in request.form:
            if not request.form['id'] or not request.form['port_device'] or not request.form['port_device_port'] or not request.form['port_mode'] or not request.form['port_vlan'] or not request.form['port_pxe_boot']:
                flash('Please fill all fields before sending a request !','danger')
                return redirect(request.url)
            else:
                if request.form['port_mode'] == 'None' and request.form['port_vlan'] == 'None':
                    port_id = request.form.get('id')
                    port = Switch1_24_port.query.filter_by(id=port_id).one()
                    port.devicename=request.form['port_device']
                    port.deviceport=request.form['port_device_port']
                    port.vlan_id = ''
                    port.portmode = 'None'
                    port.portvlan = 'None'
                    port.portpxeboot=(strtobool(request.form['port_pxe_boot']))
                    db.session.add(port)
                    db.session.commit()
                    flash('Port ' + port_id + ' Saved','success')
                    return redirect(request.url)
                if request.form['port_mode'] == 'trunk':
                    if request.form['port_vlan'] == 'trunk':
                        port_id = request.form.get('id')
                        port = Switch1_24_port.query.filter_by(id=port_id).one()
                        port.devicename=request.form['port_device']
                        port.deviceport=request.form['port_device_port']
                        port.portmode=request.form['port_mode']
                        port.portvlan = 'trunk'
                        port.portpxeboot=(strtobool(request.form['port_pxe_boot']))
                        db.session.add(port)
                        db.session.commit()
                        flash('Port ' + port_id + ' Saved','success')
                        return redirect(request.url)
                    if request.form['port_vlan'] == 'None':
                        flash('Trunk port cannot be "None" !','danger')
                        return redirect(request.url)
                    else:
                        flash('Trunk port cannot be "access" !','danger')
                        return redirect(request.url)
                elif request.form['port_mode'] == 'access':
                    if request.form['port_vlan'] == 'None' or request.form['port_vlan'] == '' or request.form['port_vlan'] == 'trunk':
                        flash('Access port cannot be "trunk" or "None" !','danger')
                        return redirect(request.url)
                    else:
                        port_id = request.form.get('id')
                        port = Switch1_24_port.query.filter_by(id=port_id).one()
                        port.devicename=request.form['port_device']
                        port.deviceport=request.form['port_device_port']
                        port.portmode=request.form['port_mode']
                        vlan_id =request.form['port_vlan']
                        vlan = Vlans.query.filter_by(id=vlan_id).one()
                        port.sw124vlansbackref = vlan
                        port.portvlan = request.form['port_vlan']
                        port.portpxeboot=(strtobool(request.form['port_pxe_boot']))
                        db.session.add(port)
                        db.session.commit()
                        flash('Port ' + port_id + ' Saved','success')
                        return redirect(request.url)
                else:
                    flash('Please fill all form fields! MODE and VLAN must be "None" to default interface.','danger')
                    return redirect(request.url)
        if 'port_config_switch1_24_port_generate' in request.form:
            if not request.form['port_config_switch1_24_port_generate'] or not request.form['switch1_24_port_version']:
                flash('Please fill all fields before sending a request !','danger')
                return redirect(request.url)
	    else:
                customer_sw1 = Customer_sw.query.filter_by(id=1).one()
                if customer_sw1.customerswbackref.portnr == '8' or customer_sw1.customerswbackref.portnr == '48':
                    flash('Your switch has ' + customer_sw1.customerswbackref.portnr + ' ports and does match the template !','danger')
                    return redirect(request.url)
                else:
                    switch1_24_port_version = request.form.get('switch1_24_port_version')
                    vlans = Vlans.query.all()
                    ports = Switch1_24_port.query.all()
                    if switch1_24_port_version == 'sw-24-Fa':
                        template_file = 'switch_templates/customer-sw-1-24-Fa-port-config.j2'
                        template_output = "output/customer-sw-1-24-portconfig.deploy"
                    elif switch1_24_port_version == 'sw-24-Gi':
                        template_file = 'switch_templates/customer-sw-1-24-Gi-port-config.j2'
                        template_output = "output/customer-sw-1-24-portconfig.deploy"
                    env = Environment(loader=FileSystemLoader(TEMPLATE_CONFIG))
                    template = env.get_template(template_file)
                    generate_template = template.render(customer='HEXTRIM', ports=ports, vlans=vlans)
                    with open(template_output, "wb") as f:
                        f.write(generate_template)
                    flash('Template generated successfully !','success')
                    return redirect(request.url)
        else:
            flash('Malformed form submitted !','danger')
            return redirect(request.url)

