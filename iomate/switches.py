from jinja2 import Environment, FileSystemLoader
from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db, os
from iomate.models import Switches, Vlans, Customer_sw

switches = Blueprint('switches', __name__)

### LOCAL CONFIG ###
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = 'templates/configuration_templates/pyserial'
TEMPLATE_CONFIG = os.path.join(BASE_DIR, TEMPLATE_DIR)

@switches.route("/switches", methods=['GET', 'POST'])
@login_required
def switches_view():
    error = None
    if request.method == 'GET':
        file_switch1 = open("output/customer-sw-1-baseconfig.deploy", "r")
        lines_switch1 = file_switch1.readlines()
        file_switch2 = open("output/customer-sw-2-baseconfig.deploy", "r")
        lines_switch2 = file_switch2.readlines()
        return render_template('switches.html', sws=Switches.query.all(), vlans=Vlans.query.all(), customer_sws=Customer_sw.query.all(), lines_switch1=lines_switch1, lines_switch2=lines_switch2)
    elif request.method == 'POST':
        if 'sw_add' in request.form:
	    if not request.form['sw_hostname'] or not request.form['sw_ipaddress'] or not request.form['sw_subnet'] or not request.form['sw_gateway'] or not request.form['sw_mgmtvlan'] or not request.form['sw_portnr'] or not request.form['sw_porttype']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
		sw = Switches(request.form['sw_hostname'], request.form['sw_ipaddress'], request.form['sw_subnet'], request.form['sw_gateway'], request.form['sw_mgmtvlan'], request.form['sw_portnr'], request.form['sw_porttype'])
                db.session.add(sw)
		db.session.commit()
#		sw_hostname = request.form['sw_hostname']
#		sw = Switches.query.filter_by(hostname=sw_hostname).one()
                customer_sw_id = request.form['sw_customer_sw_map']
		if customer_sw_id == 'None':
                    pass
                else:
                    sw_hostname = request.form['sw_hostname']
                    sw = Switches.query.filter_by(hostname=sw_hostname).one()
                    customer_sw = Customer_sw.query.filter_by(id=customer_sw_id).one()
                    customer_sw.customerswbackref = sw
                    db.session.add(customer_sw)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Switch Added</div>"
        elif 'sw_edit' in request.form:
	    if not request.form['sw_hostname'] or not request.form['sw_ipaddress'] or not request.form['sw_subnet'] or not request.form['sw_gateway'] or not request.form['sw_mgmtvlan'] or not request.form['sw_portnr'] or not request.form['sw_porttype']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                sw_id = request.form.get('id')
                sw = Switches.query.filter_by(id=sw_id).one()
                sw.hostname=request.form['sw_hostname']
                sw.ipaddress=request.form['sw_ipaddress']
                sw.subnet=request.form['sw_subnet']
                sw.gateway=request.form['sw_gateway']
                sw.mgmtvlan=request.form['sw_mgmtvlan']
                sw.portnr=request.form['sw_portnr']
                sw.porttype=request.form['sw_porttype']
#                db.session.add(sw)
#                db.session.commit()
		customer_sw_id = request.form['sw_customer_sw_map']
                if customer_sw_id == 'None':
		    sw.customer_sw = ''
                    db.session.add(sw)
                    db.session.commit()
		else:
	    	    customer_sw = Customer_sw.query.filter_by(id=customer_sw_id).one()
                    customer_sw.customerswbackref = sw
                    db.session.add(sw)
                    db.session.add(customer_sw)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Switch Edited</div>"
        elif 'sw_delete' in request.form:
            if not request.form['sw_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                sw_id = request.form.getlist('id')
                for u in sw_id:
                    sw  = Switches.query.filter_by(id=u).one()
                    db.session.delete(sw)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Switch Deleted</div>"
        elif 'base_config_switch1_generate' in request.form:
            if not request.form['base_config_switch1_generate'] or not request.form['switch1_profile']:
                flash('Please fill all fields before sending a request !','danger')
                return redirect(request.url)
            else:
                switch1_profile = request.form.get('switch1_profile')
                switch1 = Switches.query.filter_by(id=switch1_profile).one()
                template_file = 'switch_templates/customer-sw-1-base-config.j2'
                template_output = "output/customer-sw-1-baseconfig.deploy"
                env = Environment(loader=FileSystemLoader(TEMPLATE_CONFIG))
                template = env.get_template(template_file)
		generate_template = template.render(customer_sw_1=switch1.hostname, customer_sw_1_mgmt_ipadress=switch1.ipaddress, customer_sw_1_mgmt_subnet=switch1.subnet, customer_sw_1_mgmt_gateway=switch1.gateway, mgmt_vlan_id=switch1.mgmtvlan)
                with open(template_output, "wb") as f:
                    f.write(generate_template)
                flash('Template generated successfully !','success')
                return redirect(request.url)
        elif 'base_config_switch2_generate' in request.form:
            if not request.form['base_config_switch2_generate'] or not request.form['switch2_profile']:
                flash('Please fill all fields before sending a request !','danger')
                return redirect(request.url)
            else:
                switch2_profile = request.form.get('switch2_profile')
                switch2 = Switches.query.filter_by(id=switch2_profile).one()
                template_file = 'switch_templates/customer-sw-2-base-config.j2'
                template_output = "output/customer-sw-2-baseconfig.deploy"
                env = Environment(loader=FileSystemLoader(TEMPLATE_CONFIG))
                template = env.get_template(template_file)
		generate_template = template.render(customer_sw_2=switch2.hostname, customer_sw_2_mgmt_ipadress=switch2.ipaddress, customer_sw_2_mgmt_subnet=switch2.subnet, customer_sw_2_mgmt_gateway=switch2.gateway, mgmt_vlan_id=switch2.mgmtvlan)
                with open(template_output, "wb") as f:
                    f.write(generate_template)
                flash('Template generated successfully !','success')
                return redirect(request.url)
    return render_template('switches.html')
