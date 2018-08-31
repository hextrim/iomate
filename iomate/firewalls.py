from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import Firewalls

firewalls = Blueprint('firewalls', __name__)

@firewalls.route("/firewalls", methods=['GET', 'POST'])
@login_required
def firewalls_view():
    error = None
    if request.method == 'GET':
        return render_template('firewalls.html', fws=Firewalls.query.all())
    elif request.method == 'POST':
        if 'fw_add' in request.form:
            if not request.form['fw_hostname'] or not request.form['fw_ipaddress'] or not request.form['fw_subnet'] or not request.form['fw_gateway'] or not request.form['fw_mgmtnetwork'] or not request.form['fw_mgmtsubnet']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                fw = Firewalls(request.form['fw_hostname'], request.form['fw_ipaddress'], request.form['fw_subnet'], request.form['fw_gateway'], request.form['fw_mgmtnetwork'], request.form['fw_mgmtsubnet'])
                db.session.add(fw)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Firewall Added</div>"
        elif 'fw_edit' in request.form:
            if not request.form['fw_hostname'] or not request.form['fw_ipaddress'] or not request.form['fw_subnet'] or not request.form['fw_gateway'] or not request.form['fw_mgmtnetwork'] or not request.form['fw_mgmtsubnet']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                fw_id = request.form.get('id')
                fw = Firewalls.query.filter_by(id=fw_id).one()
                fw.hostname=request.form['fw_hostname']
                fw.ipaddress=request.form['fw_ipaddress']
                fw.subnet=request.form['fw_subnet']
                fw.gateway=request.form['fw_gateway']
                fw.mgmtnetwork=request.form['fw_mgmtnetwork']
                fw.mgmtsubnet=request.form['fw_mgmtsubnet']
                db.session.add(fw)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Firewall Edited</div>"
        elif 'fw_delete' in request.form:
            if not request.form['fw_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                fw_id = request.form.getlist('id')
                for u in fw_id:
                    fw  = Firewalls.query.filter_by(id=u).one()
                    db.session.delete(fw)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Firewall Deleted</div>"
    return render_template('firewalls.html')

