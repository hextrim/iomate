from jinja2 import Environment, FileSystemLoader
import jenkins
import codecs

from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, os, socketio, roles_required
from iomate.models import Switches, Switch1_24_port, Switch2_24_port, Switch1_48_port, Switch2_48_port, Customer_sw

##IMPORT FROM IOMATE GLOBAL##
from iomate.iomate_global import srvjenkins
from iomate.iomate_global import get_deploy_device_last_build_log
from iomate.iomate_global import get_deploy_device_get_job_info
from iomate.iomate_global import cct_swx


deploy_switch = Blueprint('deploy_switch', __name__)

### LOCAL CONFIG ###
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = 'templates/configuration_templates/pyserial'
TEMPLATE_CONFIG = os.path.join(BASE_DIR, TEMPLATE_DIR)

@deploy_switch.route("/deploy-switch", methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def deploy_switch_view():
    error = None
    if request.method == 'GET':
        socketio.start_background_task(cct_swx, '/dev/ttyUSB0', 'sw1usbsignal', 'sw1portsignal')
        socketio.start_background_task(cct_swx, '/dev/ttyUSB1', 'sw2usbsignal', 'sw2portsignal')
        deploy_sw_1_baseconfig = get_deploy_device_last_build_log('deploy_sw_1_baseconfig')
        deploy_sw_1_baseconfig_job_info = get_deploy_device_get_job_info('deploy_sw_1_baseconfig')
        deploy_sw_1_portconfig = get_deploy_device_last_build_log('deploy_sw_1_portconfig')
        deploy_sw_1_portconfig_job_info = get_deploy_device_get_job_info('deploy_sw_1_portconfig')
        deploy_sw_1_singleport = get_deploy_device_last_build_log('deploy_sw_1_singleport')
        deploy_sw_1_singleport_job_info = get_deploy_device_get_job_info('deploy_sw_1_singleport')
        return render_template('deploy-switch.html', deploy_sw_1_baseconfig=deploy_sw_1_baseconfig, deploy_sw_1_baseconfig_job_info=deploy_sw_1_baseconfig_job_info, deploy_sw_1_portconfig=deploy_sw_1_portconfig, deploy_sw_1_portconfig_job_info=deploy_sw_1_portconfig_job_info, deploy_sw_1_singleport=deploy_sw_1_singleport, deploy_sw_1_singleport_job_info=deploy_sw_1_singleport_job_info, sws=Switches.query.all(), customer_sws=Customer_sw.query.all())
    elif request.method == 'POST':
        if 'deploy_switch1_config_deploy' in request.form:
            if not request.form['deploy_switch1_device'] or not request.form['deploy_switch1_config']:
                flash('Please fill all the fields before sending a request!','danger')
                return redirect(request.url)
            else:
                sw1_device = request.form['deploy_switch1_device']
                sw1_config = request.form['deploy_switch1_config']
                sw1 = Switches.query.filter_by(id=sw1_device).one()
                if sw1_config == 'baseconfig':
                    srvjobs = srvjenkins.get_jobs()
                    config_xml = "output/deploy-sw-1-baseconfig.xml"
                    with codecs.open(config_xml,'r',encoding='utf8') as f:
                        config_xml_file = f.read()
                    match = any(s['name'] == 'deploy_sw_1_baseconfig' for s in srvjobs)
                    if match == True:
                        srvjenkins.reconfig_job('deploy_sw_1_baseconfig', config_xml_file)
                    else:
                        srvjenkins.create_job('deploy_sw_1_baseconfig', config_xml_file)
                    srvjenkins.build_job('deploy_sw_1_baseconfig')
                    flash('Deploy BASECONFIG task has been submitted and started.','success')
                    return redirect(request.url)
                elif sw1_config == 'portconfig' and sw1.portnr == '24':
                    srvjobs = srvjenkins.get_jobs()
                    config_xml = "output/deploy-sw-1-24-portconfig.xml"
                    with codecs.open(config_xml,'r',encoding='utf8') as f:
                        config_xml_file = f.read()
                    match = any(s['name'] == 'deploy_sw_1_portconfig' for s in srvjobs)
                    if match == True:
                        srvjenkins.reconfig_job('deploy_sw_1_portconfig', config_xml_file)
                    else:
                        srvjenkins.create_job('deploy_sw_1_portconfig', config_xml_file)
                    srvjenkins.build_job('deploy_sw_1_portconfig')
                    flash('Deploy PORTCONFIG task for 24 port switch has been submitted and started.','success')
                    return redirect(request.url)
                elif sw1_config == 'portconfig' and sw1.portnr == '48':
                    srvjobs = srvjenkins.get_jobs()
                    config_xml = "output/deploy-sw-1-48-portconfig.xml"
                    with codecs.open(config_xml,'r',encoding='utf8') as f:
                        config_xml_file = f.read()
                    match = any(s['name'] == 'deploy_sw_1_portconfig' for s in srvjobs)
                    if match == True:
                        srvjenkins.reconfig_job('deploy_sw_1_portconfig', config_xml_file)
                    else:
                        srvjenkins.create_job('deploy_sw_1_portconfig', config_xml_file)
                    srvjenkins.build_job('deploy_sw_1_portconfig')
                    flash('Deploy PORTCONFIG task for 48 port switch has been submitted and started.','success')
                    return redirect(request.url)
                elif int(sw1_config) in range(1,48):
                    if sw1.portnr == '24' and sw1.porttype == 'Fa':
                        port = Switch1_24_port.query.filter_by(id=sw1_config).one()
                        template_file = 'switch_templates/customer-sw-1-24-Fa-singleport-config.j2'
                        template_output = "output/customer-sw-1-singleport.deploy"
                        env = Environment(loader=FileSystemLoader(TEMPLATE_CONFIG))
                        template = env.get_template(template_file)
                        generate_template = template.render(port=port)
                        with open(template_output, "wb") as f:
                            f.write(generate_template)
                        srvjobs = srvjenkins.get_jobs()
                        config_xml = "output/deploy-sw-1-singleport.xml"
                        with codecs.open(config_xml,'r',encoding='utf8') as f:
                            config_xml_file = f.read()
                        match = any(s['name'] == 'deploy_sw_1_singleport' for s in srvjobs)
                        if match == True:
                            srvjenkins.reconfig_job('deploy_sw_1_singleport', config_xml_file)
                        else:
                            srvjenkins.create_job('deploy_sw_1_singleport', config_xml_file)
                        srvjenkins.build_job('deploy_sw_1_singleport')
                        flash('Deploy SINGLEPORT P' + sw1_config + ' task has been submitted and started.','success')
                        return redirect(request.url)
                    elif sw1.portnr == '24' and sw1.porttype == 'Gi':
                        port = Switch1_24_port.query.filter_by(id=sw1_config).one()
                        template_file = 'switch_templates/customer-sw-1-24-Gi-singleport-config.j2'
                        template_output = "output/customer-sw-1-singleport.deploy"
                        env = Environment(loader=FileSystemLoader(TEMPLATE_CONFIG))
                        template = env.get_template(template_file)
                        generate_template = template.render(port=port)
                        with open(template_output, "wb") as f:
                            f.write(generate_template)
                        srvjobs = srvjenkins.get_jobs()
                        config_xml = "output/deploy-sw-1-singleport.xml"
                        with codecs.open(config_xml,'r',encoding='utf8') as f:
                            config_xml_file = f.read()
                        match = any(s['name'] == 'deploy_sw_1_singleport' for s in srvjobs)
                        if match == True:
                            srvjenkins.reconfig_job('deploy_sw_1_singleport', config_xml_file)
                        else:
                            srvjenkins.create_job('deploy_sw_1_singleport', config_xml_file)
                        srvjenkins.build_job('deploy_sw_1_singleport')
                        flash('Deploy SINGLEPORT P' + sw1_config + ' task has been submitted and started.','success')
                        return redirect(request.url)
                    elif sw1.portnr == '48' and sw1.porttype == 'Fa':
                        port = Switch1_48_port.query.filter_by(id=sw1_config).one()
                    elif sw1.portnr == '48' and sw1.porttype == 'Gi':
                        port = Switch1_48_port.query.filter_by(id=sw1_config).one()

                    flash('Deploy SINGLEPORT P' + sw1_config + ' task has been submitted and started.','success')
                    return redirect(request.url)
                else:
                    flash('Oops something went wrong !','danger')
                    return redirect(request.url)

        elif 'deploy_switch2_config_deploy' in request.form:
            if not request.form['deploy_switch2_device'] or not request.form['deploy_switch2_config']:
                flash('Please fill all the fields before sending a request!','danger')
                return redirect(request.url)
            else:
                sw2_device = request.form['deploy_switch2_device']
                sw2_config = request.form['deploy_switch2_config']
                sw2 = Switches.query.filter_by(id=sw2_device).one()
                if sw2_config == 'baseconfig':
                    srvjobs = srvjenkins.get_jobs()
                    config_xml = "output/deploy-sw-2-baseconfig.xml"
                    with codecs.open(config_xml,'r',encoding='utf8') as f:
                        config_xml_file = f.read()
                    match = any(s['name'] == 'deploy_sw_2_baseconfig' for s in srvjobs)
                    if match == True:
                        srvjenkins.reconfig_job('deploy_sw_2_baseconfig', config_xml_file)
                    else:
                        srvjenkins.create_job('deploy_sw_2_baseconfig', config_xml_file)
                    srvjenkins.build_job('deploy_sw_2_baseconfig')
                    flash('Deploy BASECONFIG task has been submitted and started.','success')
                    return redirect(request.url)
                elif sw2_config == 'portconfig' and sw2.portnr == '24':
                    srvjobs = srvjenkins.get_jobs()
                    config_xml = "output/deploy-sw-2-24-portconfig.xml"
                    with codecs.open(config_xml,'r',encoding='utf8') as f:
                        config_xml_file = f.read()
                    match = any(s['name'] == 'deploy_sw_2_portconfig' for s in srvjobs)
                    if match == True:
                        srvjenkins.reconfig_job('deploy_sw_2_portconfig', config_xml_file)
                    else:
                        srvjenkins.create_job('deploy_sw_2_portconfig', config_xml_file)
                    srvjenkins.build_job('deploy_sw_2_portconfig')
                    flash('Deploy PORTCONFIG task for 24 port switch has been submitted and started.','success')
                    return redirect(request.url)
                elif sw2_config == 'portconfig' and sw2.portnr == '48':
                    srvjobs = srvjenkins.get_jobs()
                    config_xml = "output/deploy-sw-2-48-portconfig.xml"
                    with codecs.open(config_xml,'r',encoding='utf8') as f:
                        config_xml_file = f.read()
                    match = any(s['name'] == 'deploy_sw_2_portconfig' for s in srvjobs)
                    if match == True:
                        srvjenkins.reconfig_job('deploy_sw_2_portconfig', config_xml_file)
                    else:
                        srvjenkins.create_job('deploy_sw_2_portconfig', config_xml_file)
                    srvjenkins.build_job('deploy_sw_2_portconfig')
                    flash('Deploy PORTCONFIG task for 48 port switch has been submitted and started.','success')
                    return redirect(request.url)
                elif int(sw2_config) in range(1,48):
                    if sw2.portnr == '24' and sw2.porttype == 'Fa':
                        port = Switch2_24_port.query.filter_by(id=sw2_config).one()
                        template_file = 'switch_templates/customer-sw-2-24-Fa-singleport-config.j2'
                        template_output = "output/customer-sw-2-singleport.deploy"
                        env = Environment(loader=FileSystemLoader(TEMPLATE_CONFIG))
                        template = env.get_template(template_file)
                        generate_template = template.render(port=port)
                        with open(template_output, "wb") as f:
                            f.write(generate_template)
                        srvjobs = srvjenkins.get_jobs()
                        config_xml = "output/deploy-sw-2-singleport.xml"
                        with codecs.open(config_xml,'r',encoding='utf8') as f:
                            config_xml_file = f.read()
                        match = any(s['name'] == 'deploy_sw_2_singleport' for s in srvjobs)
                        if match == True:
                            srvjenkins.reconfig_job('deploy_sw_2_singleport', config_xml_file)
                        else:
                            srvjenkins.create_job('deploy_sw_2_singleport', config_xml_file)
                        srvjenkins.build_job('deploy_sw_2_singleport')
                        flash('Deploy SINGLEPORT P' + sw2_config + ' task has been submitted and started.','success')
                        return redirect(request.url)
                    elif sw2.portnr == '24' and sw2.porttype == 'Gi':
                        port = Switch2_24_port.query.filter_by(id=sw2_config).one()
                        template_file = 'switch_templates/customer-sw-2-24-Gi-singleport-config.j2'
                        template_output = "output/customer-sw-2-singleport.deploy"
                        env = Environment(loader=FileSystemLoader(TEMPLATE_CONFIG))
                        template = env.get_template(template_file)
                        generate_template = template.render(port=port)
                        with open(template_output, "wb") as f:
                            f.write(generate_template)
                        srvjobs = srvjenkins.get_jobs()
                        config_xml = "output/deploy-sw-2-singleport.xml"
                        with codecs.open(config_xml,'r',encoding='utf8') as f:
                            config_xml_file = f.read()
                        match = any(s['name'] == 'deploy_sw_2_singleport' for s in srvjobs)
                        if match == True:
                            srvjenkins.reconfig_job('deploy_sw_2_singleport', config_xml_file)
                        else:
                            srvjenkins.create_job('deploy_sw_2_singleport', config_xml_file)
                        srvjenkins.build_job('deploy_sw_2_singleport')
                        flash('Deploy SINGLEPORT P' + sw2_config + ' task has been submitted and started.','success')
                        return redirect(request.url)
                    elif sw2.portnr == '48' and sw2.porttype == 'Fa':
                        port = Switch2_48_port.query.filter_by(id=sw2_config).one()
                    elif sw2.portnr == '48' and sw2.porttype == 'Gi':
                        port = Switch2_48_port.query.filter_by(id=sw2_config).one()

                    flash('Deploy SINGLEPORT P' + sw2_config + ' task has been submitted and started.','success')
                    return redirect(request.url)
                else:
                    flash('Oops something went wrong !','danger')
                    return redirect(request.url)

    return render_template('deploy-switch.html')

