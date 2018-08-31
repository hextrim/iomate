from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import Ips

ips = Blueprint('ips', __name__)

@ips.route("/ips", methods=['GET', 'POST'])
@login_required
def ips_view():
    error = None
    if request.method == 'GET':
        return render_template('ips.html', ipss=Ips.query.all())
    elif request.method == 'POST':
        if 'ips_add' in request.form:
            if not request.form['ips_hostname'] or not request.form['ips_ipaddress'] or not request.form['ips_subnet'] or not request.form['ips_gateway'] or not request.form['ips_username'] or not request.form['ips_password']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                ips = Ips(request.form['ips_hostname'], request.form['ips_ipaddress'], request.form['ips_subnet'], request.form['ips_gateway'], request.form['ips_username'], request.form['ips_password'])
                db.session.add(ips)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>IPS Added</div>"
        elif 'ips_edit' in request.form:
            if not request.form['ips_hostname'] or not request.form['ips_ipaddress'] or not request.form['ips_subnet'] or not request.form['ips_gateway'] or not request.form['ips_username'] or not request.form['ips_password']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                ips_id = request.form.get('id')
                ips = Ips.query.filter_by(id=ips_id).one()
                ips.hostname=request.form['ips_hostname']
                ips.ipaddress=request.form['ips_ipaddress']
                ips.subnet=request.form['ips_subnet']
                ips.gateway=request.form['ips_gateway']
                ips.username=request.form['ips_username']
                ips.password=request.form['ips_password']
                db.session.add(ips)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>IPS Edited</div>"
        elif 'ips_delete' in request.form:
            if not request.form['ips_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                ips_id = request.form.getlist('id')
                for u in ips_id:
                    ips  = Ips.query.filter_by(id=u).one()
                    db.session.delete(ips)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>IPS Deleted</div>"
    return render_template('ips.html')

