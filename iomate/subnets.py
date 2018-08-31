from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import Subnets, Vlans

subnets = Blueprint('subnets', __name__)


@subnets.route("/subnets", methods=['GET', 'POST'])
@login_required
def subnets_view():
    error = None
    if request.method == 'GET':
        return render_template('subnets.html', subnets=Subnets.query.all(), vlans=Vlans.query.all())
    elif request.method == 'POST':
        if 'subnet_add' in request.form:
            if not request.form['subnet_name'] or not request.form['subnet_network'] or not request.form['subnet_mask']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                subnet = Subnets(request.form['subnet_name'], request.form['subnet_network'], request.form['subnet_mask'])
                db.session.add(subnet)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Subnet Added</div>"
        elif 'subnet_edit' in request.form:
            if not request.form['subnet_name'] or not request.form['subnet_network'] or not request.form['subnet_mask']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                subnet_id = request.form.get('id')
                subnet = Subnets.query.filter_by(id=subnet_id).one()
                subnet.name=request.form['subnet_name']
                subnet.network=request.form['subnet_network']
                subnet.mask=request.form['subnet_mask']
                db.session.add(subnet)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Subnet Edited</div>"
        elif 'subnet_delete' in request.form:
            if not request.form['subnet_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                subnet_id = request.form.getlist('id')
                for u in subnet_id:
                    subnet  = Subnets.query.filter_by(id=u).one()
                    db.session.delete(subnet)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Subnet Deleted</div>"
    return render_template('subnets.html')

