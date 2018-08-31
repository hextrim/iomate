from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import Dedicatedsan

dedicatedsan = Blueprint('dedicatedsan', __name__)

@dedicatedsan.route("/dedicatedsan", methods=['GET', 'POST'])
@login_required
def dedicatedsan_view():
    error = None
    if request.method == 'GET':
        return render_template('dedicatedsan.html', dedicatedsans=Dedicatedsan.query.all())
    elif request.method == 'POST':
        if 'dedicatedsan_add' in request.form:
            if not request.form['dedicatedsan_hostname'] or not request.form['dedicatedsan_ipaddress'] or not request.form['dedicatedsan_subnet'] or not request.form['dedicatedsan_gateway'] or not request.form['dedicatedsan_port'] or not request.form['dedicatedsan_provider'] or not request.form['dedicatedsan_username'] or not request.form['dedicatedsan_password']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                dedicatedsan = Dedicatedsan(request.form['dedicatedsan_hostname'], request.form['dedicatedsan_ipaddress'], request.form['dedicatedsan_subnet'], request.form['dedicatedsan_gateway'], request.form['dedicatedsan_port'], request.form['dedicatedsan_provider'], request.form['dedicatedsan_username'], request.form['dedicatedsan_password'])
                db.session.add(dedicatedsan)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>DedicatedSAN Added</div>"
        elif 'dedicatedsan_edit' in request.form:
            if not request.form['dedicatedsan_hostname'] or not request.form['dedicatedsan_ipaddress'] or not request.form['dedicatedsan_subnet'] or not request.form['dedicatedsan_gateway'] or not request.form['dedicatedsan_port'] or not request.form['dedicatedsan_provider'] or not request.form['dedicatedsan_username'] or not request.form['dedicatedsan_password']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                dedicatedsan_id = request.form.get('id')
                dedicatedsan = Dedicatedsan.query.filter_by(id=dedicatedsan_id).one()
                dedicatedsan.hostname=request.form['dedicatedsan_hostname']
                dedicatedsan.ipaddress=request.form['dedicatedsan_ipaddress']
                dedicatedsan.subnet=request.form['dedicatedsan_subnet']
                dedicatedsan.gateway=request.form['dedicatedsan_gateway']
                dedicatedsan.port=request.form['dedicatedsan_port']
                dedicatedsan.provider=request.form['dedicatedsan_provider']
                dedicatedsan.username=request.form['dedicatedsan_username']
                dedicatedsan.password=request.form['dedicatedsan_password']
                db.session.add(dedicatedsan)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Dedicatedsan Edited</div>"
        elif 'dedicatedsan_delete' in request.form:
            if not request.form['dedicatedsan_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                dedicatedsan_id = request.form.getlist('id')
                for u in dedicatedsan_id:
                    dedicatedsan = Dedicatedsan.query.filter_by(id=u).one()
                    db.session.delete(dedicatedsan)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Dedicatedsan Deleted</div>"
    return render_template('dedicatedsan.html')
