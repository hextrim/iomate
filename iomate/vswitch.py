from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import Vsswitch

vswitch = Blueprint('vswitch', __name__)

@vswitch.route("/vswitch", methods=['GET', 'POST'])
@login_required
def vswitch_view():
    error = None
    if request.method == 'GET':
        return render_template('vswitch.html', vss=Vsswitch.query.all())
    elif request.method == 'POST':
        if 'vs_add' in request.form:
            if not request.form['vs_name'] or not request.form['vs_ipaddress'] or not request.form['vs_subnet'] or not request.form['vs_gateway'] or not request.form['vs_nic1'] or not request.form['vs_nic2']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vs = Vsswitch(request.form['vs_name'], request.form['vs_ipaddress'], request.form['vs_subnet'], request.form['vs_gateway'], request.form['vs_nic1'], request.form['vs_nic2'])
                db.session.add(vs)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>vS Added</div>"
        elif 'vs_edit' in request.form:
            if not request.form['vs_name'] or not request.form['vs_ipaddress'] or not request.form['vs_subnet'] or not request.form['vs_gateway'] or not request.form['vs_nic1'] or not request.form['vs_nic2']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vs_id = request.form.get('id')
                vs = Vsswitch.query.filter_by(id=vs_id).one()
                vs.name=request.form['vs_name']
                vs.ipaddress=request.form['vs_ipaddress']
                vs.subnet=request.form['vs_subnet']
                vs.gateway=request.form['vs_gateway']
                vs.nic1=request.form['vs_nic1']
                vs.nic2=request.form['vs_nic2']
                db.session.add(vs)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>vS Edited</div>"
        elif 'vs_delete' in request.form:
            if not request.form['vs_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vs_id = request.form.getlist('id')
                for u in vs_id:
                    vs  = Vsswitch.query.filter_by(id=u).one()
                    db.session.delete(vs)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>vS Deleted</div>"
    return render_template('vswitch.html')

