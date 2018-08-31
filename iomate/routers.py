from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import Routers

routers = Blueprint('routers', __name__)

@routers.route("/routers", methods=['GET', 'POST'])
@login_required
def routers_view():
    error = None
    if request.method == 'GET':
        return render_template('routers.html', routers=Routers.query.all())
    elif request.method == 'POST':
        if 'router_add' in request.form:
            if not request.form['router_hostname'] or not request.form['router_ipaddress'] or not request.form['router_subnet'] or not request.form['router_gateway'] or not request.form['router_mgmtport']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                router = Routers(request.form['router_hostname'], request.form['router_ipaddress'], request.form['router_subnet'], request.form['router_gateway'], request.form['router_mgmtport'])
                db.session.add(router)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Router Added</div>"
        elif 'router_edit' in request.form:
            if not request.form['router_hostname'] or not request.form['router_ipaddress'] or not request.form['router_subnet'] or not request.form['router_gateway'] or not request.form['router_mgmtport']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                router_id = request.form.get('id')
                router = Routers.query.filter_by(id=router_id).one()
                router.hostname=request.form['router_hostname']
                router.ipaddress=request.form['router_ipaddress']
                router.subnet=request.form['router_subnet']
                router.gateway=request.form['router_gateway']
                router.mgmtnetwork=request.form['router_mgmtport']
                db.session.add(router)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Router Edited</div>"
        elif 'router_delete' in request.form:
            if not request.form['router_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                router_id = request.form.getlist('id')
                for u in router_id:
                    router = Routers.query.filter_by(id=u).one()
                    db.session.delete(router)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Router Deleted</div>"
    return render_template('routers.html')

