from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import Vcenter

vcenter = Blueprint('vcenter', __name__)

@vcenter.route("/vcenter", methods=['GET', 'POST'])
@login_required
def vcenter_view():
    error = None
    if request.method == 'GET':
        return render_template('vcenter.html', vcs=Vcenter.query.all())
    elif request.method == 'POST':
        if 'vc_add' in request.form:
            if not request.form['vc_hostname'] or not request.form['vc_ipaddress'] or not request.form['vc_subnet'] or not request.form['vc_gateway'] or not request.form['vc_username'] or not request.form['vc_password']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vc = Vcenter(request.form['vc_hostname'], request.form['vc_ipaddress'], request.form['vc_subnet'], request.form['vc_gateway'], request.form['vc_username'], request.form['vc_password'])
                db.session.add(vc)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>vCenter Added</div>"
        elif 'vc_edit' in request.form:
            if not request.form['vc_hostname'] or not request.form['vc_ipaddress'] or not request.form['vc_subnet'] or not request.form['vc_gateway'] or not request.form['vc_username'] or not request.form['vc_password']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vc_id = request.form.get('id')
                vc = Vcenter.query.filter_by(id=vc_id).one()
                vc.hostname=request.form['vc_hostname']
                vc.ipaddress=request.form['vc_ipaddress']
                vc.subnet=request.form['vc_subnet']
                vc.gateway=request.form['vc_gateway']
                vc.username=request.form['vc_username']
                vc.password=request.form['vc_password']
                db.session.add(vc)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>vCenter Edited</div>"
        elif 'vc_delete' in request.form:
            if not request.form['vc_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vc_id = request.form.getlist('id')
                for u in vc_id:
                    vc  = Vcenter.query.filter_by(id=u).one()
                    db.session.delete(vc)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>vCenter Deleted</div>"
    return render_template('vcenter.html')
