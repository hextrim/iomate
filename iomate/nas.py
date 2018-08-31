from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import Nas

nas = Blueprint('nas', __name__)

@nas.route("/nas", methods=['GET', 'POST'])
@login_required
def nas_view():
    error = None
    if request.method == 'GET':
        return render_template('nas.html', nass=Nas.query.all())
    elif request.method == 'POST':
        if 'nas_add' in request.form:
            if not request.form['nas_hostname'] or not request.form['nas_ipaddress'] or not request.form['nas_subnet'] or not request.form['nas_gateway'] or not request.form['nas_port'] or not request.form['nas_provider'] or not request.form['nas_username'] or not request.form['nas_password']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                nas = Nas(request.form['nas_hostname'], request.form['nas_ipaddress'], request.form['nas_subnet'], request.form['nas_gateway'], request.form['nas_port'], request.form['nas_provider'], request.form['nas_username'], request.form['nas_password'])
                db.session.add(nas)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>NAS Added</div>"
        elif 'nas_edit' in request.form:
            if not request.form['nas_hostname'] or not request.form['nas_ipaddress'] or not request.form['nas_subnet'] or not request.form['nas_gateway'] or not request.form['nas_port'] or not request.form['nas_provider'] or not request.form['nas_username'] or not request.form['nas_password']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                nas_id = request.form.get('id')
                nas = Nas.query.filter_by(id=nas_id).one()
                nas.hostname=request.form['nas_hostname']
                nas.ipaddress=request.form['nas_ipaddress']
                nas.subnet=request.form['nas_subnet']
                nas.gateway=request.form['nas_gateway']
                nas.port=request.form['nas_port']
                nas.provider=request.form['nas_provider']
                nas.username=request.form['nas_username']
                nas.password=request.form['nas_password']
                db.session.add(nas)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>NAS Edited</div>"
        elif 'nas_delete' in request.form:
            if not request.form['nas_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                nas_id = request.form.getlist('id')
                for u in nas_id:
                    nas = Nas.query.filter_by(id=u).one()
                    db.session.delete(nas)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>NAS Deleted</div>"
    return render_template('nas.html')

