from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import Servers

servers = Blueprint('servers', __name__)

@servers.route("/servers", methods=['GET', 'POST'])
@login_required
def servers_view():
    error = None
    if request.method == 'GET':
        return render_template('servers.html', servers=Servers.query.all())
    elif request.method == 'POST':
        if 'server_add' in request.form:
            if not request.form['server_hostname'] or not request.form['server_ipaddress'] or not request.form['server_subnet'] or not request.form['server_gateway'] or not request.form['server_username'] or not request.form['server_password']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                server = Servers(request.form['server_hostname'], request.form['server_ipaddress'], request.form['server_subnet'], request.form['server_gateway'], request.form['server_username'], request.form['server_password'])
                db.session.add(server)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Server Added</div>"
        elif 'server_edit' in request.form:
            if not request.form['server_hostname'] or not request.form['server_ipaddress'] or not request.form['server_subnet'] or not request.form['server_gateway'] or not request.form['server_username'] or not request.form['server_password']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                server_id = request.form.get('id')
                server = Servers.query.filter_by(id=server_id).one()
                server.hostname=request.form['server_hostname']
                server.ipaddress=request.form['server_ipaddress']
                server.subnet=request.form['server_subnet']
                server.gateway=request.form['server_gateway']
                server.username=request.form['server_username']
                server.password=request.form['server_password']
                db.session.add(server)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Server Edited</div>"
        elif 'server_delete' in request.form:
            if not request.form['server_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                server_id = request.form.getlist('id')
                for u in server_id:
                    server  = Servers.query.filter_by(id=u).one()
                    db.session.delete(server)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Servers Deleted</div>"
    return render_template('servers.html')
