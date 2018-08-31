from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import Esxis

esxi = Blueprint('esxi', __name__)

@esxi.route("/esxi", methods=['GET', 'POST'])
@login_required
def esxi_view():
    error = None
    if request.method == 'GET':
        return render_template('esxi.html', esxis=Esxis.query.all())
    elif request.method == 'POST':
        if 'esxi_add' in request.form:
            if not request.form['esxi_hostname'] or not request.form['esxi_ipaddress'] or not request.form['esxi_subnet'] or not request.form['esxi_gateway'] or not request.form['esxi_username'] or not request.form['esxi_password']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                esxi = Esxis(request.form['esxi_hostname'], request.form['esxi_ipaddress'], request.form['esxi_subnet'], request.form['esxi_gateway'], request.form['esxi_username'], request.form['esxi_password'])
                db.session.add(esxi)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ESXi Added</div>"
        elif 'esxi_edit' in request.form:
            if not request.form['esxi_hostname'] or not request.form['esxi_ipaddress'] or not request.form['esxi_subnet'] or not request.form['esxi_gateway'] or not request.form['esxi_username'] or not request.form['esxi_password']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                esxi_id = request.form.get('id')
                esxi = Esxis.query.filter_by(id=esxi_id).one()
                esxi.hostname=request.form['esxi_hostname']
                esxi.ipaddress=request.form['esxi_ipaddress']
                esxi.subnet=request.form['esxi_subnet']
                esxi.gateway=request.form['esxi_gateway']
                esxi.username=request.form['esxi_username']
                esxi.password=request.form['esxi_password']
                db.session.add(esxi)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ESXi Edited</div>"
        elif 'esxi_delete' in request.form:
            if not request.form['esxi_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                esxi_id = request.form.getlist('id')
                for u in esxi_id:
                    esxi = Esxis.query.filter_by(id=u).one()
                    db.session.delete(esxi)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ESXi Deleted</div>"
    return render_template('esxi.html')
