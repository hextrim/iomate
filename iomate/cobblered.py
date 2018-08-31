from iomate.iomate_app import app, Blueprint, render_template, request, flash, redirect, login_required, roles_required, db, os
from iomate.models import Isos
import xmlrpclib
from xmlrpclib import *
import re
import fileinput

cobblered = Blueprint('cobblered', __name__)

### LOCAL CONFIG ###
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

### COBBLER ###
##TO DO: redo cobbler_server with BootAPI()
cobbler_server = xmlrpclib.Server("http://192.168.1.83/cobbler_api")
token = cobbler_server.login("cobbler", "cobbler")

def cobbler_config_replace(string, var):
    cobbler_config_file = fileinput.FileInput("/etc/cobbler/dhcp.template", inplace=True)
    for line in cobbler_config_file:
        line = re.sub(r"(" + string + ")+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", string + " " + var + " ", line.rstrip())
        print(line)
#cobbler_config_replace("netmask", "netmask 255.0.0.0 ")

def cobbler_import(import_iso_date):
    while True:
        something = cobbler_server.get_events()
        for event in something:
            r = re.compile("" + import_iso_date  + ".*")
            event = filter(r.match, something)
        print event[0]
        event_result = cobbler_server.get_task_status(event[0])
        print event_result[2]
        if event_result[2] == 'complete':
            break
        elif event_result[2] == 'failed':
            break
    return event_result[2], event[0]

def cobbler_os_name_find(cobbler_task_name):
    cobbler_distro_name_find = cobbler_server.get_event_log(cobbler_task_name)
    cobbler_distro_name_find_regex = re.compile(r"distro:.*?\n", re.DOTALL|re.MULTILINE)
    cobbler_distro_name_find_regex_match = cobbler_distro_name_find_regex.search(cobbler_distro_name_find)
    cobbler_distro_name_find_regex_substitute = re.sub("distro: ", "", cobbler_distro_name_find_regex_match.group(0)).rstrip()
    return cobbler_distro_name_find_regex_substitute

@cobblered.route("/cobbler", methods=['GET', 'POST'])
@login_required
def cobbler_view():
    error = None
    if request.method == 'GET':
        file_dhcp = open("/etc/cobbler/dhcp.template", "r")
        lines_dhcp = file_dhcp.readlines()
        lines_dhcp = lines_dhcp[20:25]
        file_pxe = open("/etc/cobbler/pxe/pxedefault.template", "r")
        lines_pxe = file_pxe.readlines()
        list_of_distros = cobbler_server.get_distros()
        list_of_profiles = cobbler_server.get_profiles()
        return render_template('cobbler.html', lines_dhcp=lines_dhcp, lines_pxe=lines_pxe, list_of_distros=list_of_distros, list_of_profiles=list_of_profiles, isos=Isos.query.all())
    elif request.method == 'POST':
        if 'cobbler_change_dhcp_subnet_save' in request.form:
            if not request.form['cobbler_dhcp_subnet'] or request.form['cobbler_dhcp_subnet'] == '':
                flash('Please fill all the fields before sending a request!','danger')
                return redirect(request.url)
            else:
                cobbler_dhcp_subnet = request.form['cobbler_dhcp_subnet']
#               cobbler_config_file = fileinput.FileInput("/etc/cobbler/dhcp.template", inplace=True)
#                cobbler_dhcp_subnet_string = "subnet " + cobbler_dhcp_subnet + " "
#                for line in cobbler_config_file:
#                    line = re.sub(r"(subnet)+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", cobbler_dhcp_subnet_string, line.rstrip())
#                   print(line)
# print(line) is required as without it, the whole file may go truncated - replaces with blank input - removed
                cobbler_config_replace("subnet", cobbler_dhcp_subnet)
                flash('Your Cobbler DHCP Subnet has been changed.','success')
                return redirect(request.url)
        elif 'cobbler_change_dhcp_subnet_mask_save' in request.form:
            if not request.form['cobbler_dhcp_subnet_mask'] or request.form['cobbler_dhcp_subnet_mask'] == '':
                flash('Please fill all the fields before sending a request!','danger')
                return redirect(request.url)
            else:
                cobbler_dhcp_subnet_mask = request.form['cobbler_dhcp_subnet_mask']
                cobbler_config_replace("netmask", cobbler_dhcp_subnet_mask)
                cobbler_config_replace("subnet-mask", cobbler_dhcp_subnet_mask + ";")
                flash('Your Cobbler DHCP Subnet Mask details have been changed.','success')
                return redirect(request.url)
        elif 'cobbler_change_router_save' in request.form:
            if not request.form['cobbler_router'] or request.form['cobbler_router'] == '':
                flash('Please fill all the fields before sending a request!','danger')
                return redirect(request.url)
            else:
                cobbler_router = request.form['cobbler_router']
                cobbler_config_replace("routers", cobbler_router + ";")
                flash('Your Cobbler Router details have been changed.','success')
                return redirect(request.url)
        elif 'cobbler_change_dhcp_dns_server_save' in request.form:
            if not request.form['cobbler_dhcp_dns_server'] or request.form['cobbler_dhcp_dns_server'] == '':
                flash('Please fill all the fields before sending a request!','danger')
                return redirect(request.url)
            else:
                cobbler_dhcp_dns_server = request.form['cobbler_dhcp_dns_server']
                cobbler_config_replace("domain-name-servers", cobbler_dhcp_dns_server + ";")
                flash('Your Cobbler DHCP DNS Server details have been changed.','success')
                return redirect(request.url)
        elif 'cobbler_change_dhcp_deployment_range_save' in request.form:
            if not request.form['cobbler_dhcp_deployment_range'] or request.form['cobbler_dhcp_deployment_range'] == '':
                flash('Please fill all the fields before sending a request!','danger')
                return redirect(request.url)
            else:
                cobbler_dhcp_deployment_range = request.form['cobbler_dhcp_deployment_range']
                cobbler_config_file = fileinput.FileInput("/etc/cobbler/dhcp.template", inplace=True)
                cobbler_dhcp_deployment_range_string = "dynamic-bootp " + cobbler_dhcp_deployment_range + ";"
                for line in cobbler_config_file:
                   line = re.sub(r"\b(dynamic-bootp)+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", cobbler_dhcp_deployment_range_string, line.rstrip(
))
                   print(line)
                flash('Your Cobbler DHCP Deployment Range details have been changed.','success')
                return redirect(request.url)
        elif 'cobbler_change_pxe_default_boot_save' in request.form:
            if not request.form['cobbler_pxe_default_boot'] or request.form['cobbler_pxe_default_boot'] == '':
                flash('Please fill all the fields before sending a request!','danger')
                return redirect(request.url)
            else:
                cobbler_pxe_default_boot = request.form['cobbler_pxe_default_boot']
                cobbler_pxe_file = fileinput.FileInput("/etc/cobbler/pxe/pxedefault.template", inplace=True)
                cobbler_pxe_default_boot_string = "ONTIMEOUT " + cobbler_pxe_default_boot
                for line in cobbler_pxe_file:
                   line = re.sub(r"^.*\b(ONTIMEOUT).*", cobbler_pxe_default_boot_string, line.rstrip())
                   print(line)
                cobbler_server.sync(token)
                flash('Your Cobbler PXE Default Boot details have been changed.','success')
                return redirect(request.url)
        elif 'cobbleriso_import' in request.form:
            if not request.form['cobbleriso_import']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Form Error</div>"
            else:
                iso_id = request.form.get('id')
                iso = Isos.query.filter_by(id=iso_id).one()
                iso_file_path = iso.filepath
                iso_mount_path = os.path.join(app.config['BASE_DIR'], iso_file_path)
                os.system("/usr/bin/mkdir /mnt/iso")
                os.system("/usr/bin/mount -o rw,loop %s /mnt/iso" % iso_mount_path)
                iso_mount_dir = "/mnt/iso"
                iso_arch = "x86_64"
                iso_full_filename = iso.filename
                iso_name = iso_full_filename.rsplit('.', 1)
                cobbler_server.background_import({ "path" : iso_mount_dir, "arch" : iso_arch, "name" : iso_name[0] }, token)
                (year, month, day, hour, minute, second, weekday, julian, dst) = time.localtime()
                iso_import_date = "%04d-%02d-%02d_%02d%02d" % (year,month,day,hour,minute)
                iso.import_eventid = iso_import_date
                cobbler_task_status, cobbler_task_name = cobbler_import(iso_import_date)
                cobbler_os_name = cobbler_os_name_find(cobbler_task_name)
#               cobbler_import(iso_import_date)
                os.system("/usr/bin/umount /mnt/iso")
#               if cobbler_import(iso_import_date) == 'complete':
                if cobbler_task_status == 'complete':
                    cobbler_server.sync(token)
                    iso.cobbler_status = 'imported'
                    iso.cobbler_name = cobbler_os_name
                    db.session.add(iso)
                    db.session.commit()
                    return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ISO Import Succeeded</div>"
                elif cobbler_import(iso_import_date) == 'failed':
                    cobbler_server.sync(token)
                    iso.cobbler_status = 'failed'
                    db.session.add(iso)
                    db.session.commit()
                    return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ISO Import Failed</div>"
        elif 'cobblerdistro_delete' in request.form:
            if not request.form['cobblerdistro_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Form Error</div>"
            else:
                cobblerdistro_name = request.form.get('id')
                iso = Isos.query.filter_by(cobbler_name=cobblerdistro_name).first()
                cobblerdistro_delete = cobbler_server.remove_distro(cobblerdistro_name, token)
                cobbler_server.sync(token)
                iso.cobbler_status = 'removed'
                db.session.add(iso)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Cobbler Distro Deleted</div>"
        elif 'cobblerprofile_delete' in request.form:
            if not request.form['cobblerprofile_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Form Error</div>"
            else:
                cobblerprofile_name = request.form.get('id')
                iso = Isos.query.filter_by(cobbler_name=cobblerprofile_name).first()
                cobblerprofile_delete = cobbler_server.remove_profile(cobblerprofile_name, token)
                cobbler_server.sync(token)
                iso.cobbler_status = 'removed'
                db.session.add(iso)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Cobbler Profile Deleted</div>"
    return render_template('cobbler.html')

