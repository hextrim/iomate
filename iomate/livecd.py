from jinja2 import Environment, FileSystemLoader
import jenkins
import codecs

from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, os

##IMPORT FROM IOMATE GLOBAL##
from iomate.iomate_global import srvjenkins
from iomate.iomate_global import get_deploy_device_last_build_log
from iomate.iomate_global import get_deploy_device_get_job_info


livecd = Blueprint('livecd', __name__)

### LOCAL CONFIG ###
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR_SALTSTACK = 'templates/configuration_templates/livecd'
TEMPLATE_CONFIG_SALTSTACK = os.path.join(BASE_DIR, TEMPLATE_DIR_SALTSTACK)

@livecd.route("/livecd", methods=['GET', 'POST'])
@login_required
def livecd_view():
    error = None
    if request.method == 'GET':
        file = open("output/hextrimos.cfg", "r")
        lines = file.readlines()
        build_hextrimos_iso = get_deploy_device_last_build_log('build_hextrimos_iso')
        build_hextrimos_iso_info = get_deploy_device_get_job_info('build_hextrimos_iso')
        convert_hextrimos_to_pxeboot = get_deploy_device_last_build_log('convert_hextrimos_to_pxeboot')
        convert_hextrimos_to_pxeboot_info = get_deploy_device_get_job_info('convert_hextrimos_to_pxeboot')
        return render_template('livecd.html', lines=lines, build_hextrimos_iso=build_hextrimos_iso, build_hextrimos_iso_info=build_hextrimos_iso_info, convert_hextrimos_to_pxeboot=convert_hextrimos_to_pxeboot, convert_hextrimos_to_pxeboot_info=convert_hextrimos_to_pxeboot_info)
    elif request.method == 'POST':
        if 'livecd_salt_master_ip_save' in request.form:
            if not request.form['livecd_salt_master_ip'] or request.form['livecd_salt_master_ip'] == '':
                flash('Please fill all the fields before sending a request!','danger')
                return redirect(request.url)
            else:
                salt_master_ip = request.form['livecd_salt_master_ip']
                template_file = 'hextrimos.j2'
                template_output = "output/hextrimos.cfg"
                env = Environment(loader=FileSystemLoader(TEMPLATE_CONFIG_SALTSTACK))
                template = env.get_template(template_file)
                generate_template = template.render(salt_master_ip=salt_master_ip)
                with open(template_output, "wb") as f:
                    f.write(generate_template)
                flash('HextrimOS configration file has been updated.','success')
                return redirect(request.url)
        elif 'build_hextrimos_iso_build' in request.form:
            if not request.form['build_hextrimos_iso_build']:
                flash('Incorrect request received!','danger')
                return redirect(request.url)
            else:
#                srvjenkins = jenkins.Jenkins('http://localhost:8080', username='iomate', password='626002e8235dfc5c049f74ce2ef012ac')
                srvjobs = srvjenkins.get_jobs()
                config_xml = "output/build-hextrimos-iso.xml"
                with codecs.open(config_xml,'r',encoding='utf8') as f:
                    config_xml_file = f.read()
                match = any(s['name'] == 'build_hextrimos_iso' for s in srvjobs)
                if match == True:
                    srvjenkins.reconfig_job('build_hextrimos_iso', config_xml_file)
                else:
                    srvjenkins.create_job('build_hextrimos_iso', config_xml_file)
                srvjenkins.build_job('build_hextrimos_iso')
                flash('Build HextrimOS ISO: Build request received!','success')
                return redirect(request.url)
        elif 'convert_hextrimos_to_pxeboot_convert' in request.form:
            if not request.form['convert_hextrimos_to_pxeboot_convert']:
                flash('Incorrect request received!','danger')
                return redirect(request.url)
            else:
#                srvjenkins = jenkins.Jenkins('http://localhost:8080', username='iomate', password='626002e8235dfc5c049f74ce2ef012ac')
                srvjobs = srvjenkins.get_jobs()
                config_xml = "output/convert-hextrimos-to-pxeboot.xml"
                with codecs.open(config_xml,'r',encoding='utf8') as f:
                    config_xml_file = f.read()
                match = any(s['name'] == 'convert_hextrimos_to_pxeboot' for s in srvjobs)
                if match == True:
                    srvjenkins.reconfig_job('convert_hextrimos_to_pxeboot', config_xml_file)
                else:
                    srvjenkins.create_job('convert_hextrimos_to_pxeboot', config_xml_file)
                srvjenkins.build_job('convert_hextrimos_to_pxeboot')
                flash('Convert HextrimOS To PXEboot: Build request received!','success')
                return redirect(request.url)
    return render_template('livecd.html')

