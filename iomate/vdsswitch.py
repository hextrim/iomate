from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import Vdsswitch

vdsswitch = Blueprint('vdsswitch', __name__)

@vdsswitch.route("/vdsswitch", methods=['GET', 'POST'])
@login_required
def vdsswitch_view():
    error = None
    if request.method == 'GET':
        return render_template('vdsswitch.html', vdss=Vdsswitch.query.all())
    elif request.method == 'POST':
        if 'vds_add' in request.form:
            if not request.form['vds_name'] or not request.form['vds_nic1'] or not request.form['vds_nic2'] or not request.form['vds_datacenter'] or not request.form['vds_portgroup'] or not request.form['vds_portgroupvlan']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vds = Vdsswitch(request.form['vds_name'], request.form['vds_nic1'], request.form['vds_nic2'], request.form['vds_datacenter'], request.form['vds_portgroup'], request.form['vds_portgroupvlan'])
                db.session.add(vds)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>vDS Added</div>"
        elif 'vds_edit' in request.form:
            if not request.form['vds_name'] or not request.form['vds_nic1'] or not request.form['vds_nic2'] or not request.form['vds_datacenter'] or not request.form['vds_portgroup'] or not request.form['vds_portgroupvlan']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vds_id = request.form.get('id')
                vds = Vdsswitch.query.filter_by(id=vds_id).one()
                vds.name=request.form['vds_name']
                vds.nic1=request.form['vds_nic1']
                vds.nic2=request.form['vds_nic2']
                vds.datacenter=request.form['vds_datacenter']
                vds.portgroup=request.form['vds_portgroup']
                vds.portgroupvlan=request.form['vds_portgroupvlan']
                db.session.add(vds)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>vDS Edited</div>"
        elif 'vds_delete' in request.form:
            if not request.form['vds_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vds_id = request.form.getlist('id')
                for u in vds_id:
                    vds  = Vdsswitch.query.filter_by(id=u).one()
                    db.session.delete(vds)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>vDS Deleted</div>"
    return render_template('vdsswitch.html')

