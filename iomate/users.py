from distutils.util import strtobool

from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, roles_required, db, encrypt_password, SQLAlchemyUserDatastore
from iomate.models import User, Role

users = Blueprint('users', __name__)

### FLASK - SECURITY ###
user_datastore = SQLAlchemyUserDatastore(db, User, Role)

@users.route("/users", methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def users_view():
    error = None
    if request.method == 'GET':
        return render_template('users.html', users=User.query.all(), roles=Role.query.all())
    elif request.method == 'POST':
        if 'user_add' in request.form:
            if not request.form['user_email'] or not request.form['user_name'] or not request.form['user_password'] or not request.form['user_active'] or not request.form['user_role']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
#                user = User(request.form['user_email'], request.form['user_name'], request.form['user_password'], request.form['user_active'], request.form['user_role'])
                rola_id = request.form['user_role']
                rola_string = Role.query.filter_by(id=rola_id).one()
                rolas = rola_string.name
		user_datastore.create_user(email=request.form['user_email'], username=request.form['user_name'], password=encrypt_password(request.form['user_password']), active=(strtobool(request.form['user_active'])), roles=[(rolas)])
#                db.session.add(user)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>User Added</div>"
        elif 'user_edit' in request.form:
            if not request.form['user_email'] or not request.form['user_name'] or not request.form['user_password'] or not request.form['user_active']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                user_id = request.form.get('id')
                user = User.query.filter_by(id=user_id).one()
                user.email=request.form['user_email']
                user.username=request.form['user_name']
                user.password=encrypt_password(request.form['user_password'])
#                user.last_login_at=request.form['user_last_login_at']
#                user.current_login_at=request.form['user_current_login_at']
#                user.last_login_ip=request.form['user_last_login_ip']
#                user.current_login_ip=request.form['user_current_login_ip']
#                user.login_count=request.form['user_login_count']
                user.active=(strtobool(request.form['user_active']))
#                rola_id = request.form['user_role']
#                rola_string = Role.query.filter_by(id=rola_id).one()
#                rolas = rola_string.name
#               user_datastore.add_role_to_user(user, rolas)
                db.session.add(user)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>User Edited</div>"
        elif 'user_role_add' in request.form:
            if not request.form['user_role']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                user_id = request.form.getlist('id')
                for u in user_id:
                    user  = User.query.filter_by(id=u).one()
                    user_email = user.email
                    find_user = user_datastore.find_user(email=user_email)
                    rola_id = request.form['user_role']
                    rola_string = Role.query.filter_by(id=rola_id).one()
                    rolas = rola_string.name
                    find_role = user_datastore.find_role(rolas)
                    user_datastore.add_role_to_user(find_user, find_role)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Role Added</div>"
        elif 'user_role_remove' in request.form:
            if not request.form['user_role']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                user_id = request.form.getlist('id')
                for u in user_id:
                    user  = User.query.filter_by(id=u).one()
                    user_email = user.email
                    find_user = user_datastore.find_user(email=user_email)
                    rola_id = request.form['user_role']
                    rola_string = Role.query.filter_by(id=rola_id).one()
                    rolas = rola_string.name
                    find_role = user_datastore.find_role(rolas)
                    user_datastore.remove_role_from_user(find_user, find_role)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Role Removed</div>"
        elif 'user_delete' in request.form:
            if not request.form['user_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                user_id = request.form.getlist('id')
                for u in user_id:
                    user  = User.query.filter_by(id=u).one()
                    db.session.delete(user)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>User Deleted</div>"
    return render_template('users.html', users=User.query.all(), roles=Role.query.all())

