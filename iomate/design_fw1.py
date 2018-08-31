from jinja2 import Environment, FileSystemLoader
from distutils.util import strtobool
from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db, os
from iomate.models import Switches, Firewalls, Esxis, Servers, Dedicatedsan, Vlans, Switch1_24_port, Customer_sw, Firewall1_interfaces, Firewall2_interfaces, Port_channels_fw1, Subnets
#from iomate.models import Firewalls, Vlans, Subnets 

design_fw1 = Blueprint('design_fw1', __name__)

### LOCAL CONFIG ###
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = 'templates/configuration_templates/pyserial'
TEMPLATE_CONFIG = os.path.join(BASE_DIR, TEMPLATE_DIR)

### DESIGN_FW1 ###
@design_fw1.route("/design-fw1", methods=['GET', 'POST'])
@login_required
def design_fw1_view():
    error = None
    if request.method == 'GET':
        file = open("output/customer-sw-1-24-portconfig.deploy", "r")
        lines = file.readlines()
#        return render_template('design-fw1.html', fws=Firewalls.query.all(), vlans=Vlans.query.all())
        return render_template('design-fw1.html', subnets=Subnets.query.all(), pochanns=Port_channels_fw1.query.all(), pos=Firewall1_interfaces.query.filter(Firewall1_interfaces.group).all(), fw_interfaces=Firewall1_interfaces.query.all(), customer_sws=Customer_sw.query.all(), vlans=Vlans.query.all(), lines=lines)
    elif request.method == 'POST':
        if 'design_fw1_port_channel_save' in request.form:
            if not request.form['design_fw1_port_channel_mode'] or not request.form.getlist['design_fw1_port_channel_interfaces']:
                flash('Please fill all fields before sending a request !','danger')
                return redirect(request.url)
            else:
                flash('Saved','success')
                return redirect(request.url)
        if 'design_fw1_port_channel_interfaces_delete' in request.form:
            if not request.form['design_fw1_port_channel_interfaces_id']:
                flash('Please fill all fields before sending a request !','danger')
                return redirect(request.url)
	    else:
                flash('Template generated successfully !','success')
                return redirect(request.url)
        if 'design_fw1_configure_interface_save' in request.form:
            if not request.form['design_fw1_configure_interface_id'] or not request.form['design_fw1_configure_interface_mode']:
                flash('Please fill all fields before sending a request !','danger')
                return redirect(request.url)
            else:
                flash('Template generated successfully !','success')
                return redirect(request.url)
        if 'design_fw1_configure_interface_delete' in request.form:
            if not request.form['design_fw1_configure_interface_id']:
                flash('Please fill all fields before sending a request !','danger')
                return redirect(request.url)
            else:
                flash('Template generated successfully !','success')
                return redirect(request.url)
        if 'design_fw1_configure_phy_interface_save' in request.form:
            if not request.form['design_fw1_configure_phy_interface_id'] or not request.form['design_fw1_configure_phy_interface_name'] or not request.form['design_fw1_configure_phy_interface_seclvl'] or not request.form['design_fw1_configure_phy_interface_subnet'] or not request.form['design_fw1_configure_phy_interface_enabled']:
                flash('Please fill all fields before sending a request !','danger')
                return redirect(request.url)
            else:
                flash('Template generated successfully !','success')
                return redirect(request.url)
        if 'design_fw1_configure_phy_interface_delete' in request.form:
            if not request.form['design_fw1_configure_phy_interface_id']:
                flash('Please fill all fields before sending a request !','danger')
                return redirect(request.url)
            else:
                flash('Template generated successfully !','success')
                return redirect(request.url)
        if 'design_fw1_configure_sub_interface_save' in request.form:
            if not request.form['design_fw1_configure_sub_interface_id'] or not request.form['design_fw1_configure_sub_interface_vlan'] or not request.form['design_fw1_configure_sub_interface_name'] or not request.form['design_fw1_configure_sub_interface_sec_lvl'] or not request.form['design_fw1_configure_sub_interface_subnet'] or not request.form['design_fw1_configure_sub_interface_enabled']:
                flash('Please fill all fields before sending a request !','danger')
                return redirect(request.url)
            else:
                flash('Template generated successfully !','success')
                return redirect(request.url)
        if 'design_fw1_configure_sub_interface_delete' in request.form:
            if not request.form['design_fw1_configure_sub_interface_id']:
                flash('Please fill all fields before sending a request !','danger')
                return redirect(request.url)
            else:
                flash('Template generated successfully !','success')
                return redirect(request.url)
        else:
            flash('Malformed form submitted !','danger')
            return redirect(request.url)

