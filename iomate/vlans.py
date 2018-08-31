from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import Vlans

vlans = Blueprint('vlans', __name__)



@vlans.route("/vlans", methods=['GET', 'POST'])
@login_required
def vlans_view():
    error = None
    if request.method == 'GET':
        return render_template('vlans.html', vlans=Vlans.query.all())
    elif request.method == 'POST':
        if 'vlan_add' in request.form:
            if not request.form['vlan_name'] or not request.form['vlan_id']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vlan = Vlans(request.form['vlan_name'], request.form['vlan_id'])
                db.session.add(vlan)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>VLAN Added</div>"
        elif 'vlan_edit' in request.form:
            if not request.form['vlan_name'] or not request.form['vlan_id']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vlan_id = request.form.get('id')
                vlan = Vlans.query.filter_by(id=vlan_id).one()
                vlan.name=request.form['vlan_name']
                vlan.vlanid=request.form['vlan_id']
                db.session.add(vlan)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>VLAN Edited</div>"
        elif 'vlan_delete' in request.form:
            if not request.form['vlan_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vlan_id = request.form.getlist('id')
                for u in vlan_id:
                    vlan  = Vlans.query.filter_by(id=u).one()
                    db.session.delete(vlan)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>VLAN Deleted</div>"
    return render_template('vlans.html')

