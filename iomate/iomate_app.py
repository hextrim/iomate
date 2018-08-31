import os
from flask import Flask, render_template, request, url_for, flash, copy_current_request_context, redirect, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required, roles_required, current_user
from flask_security.utils import encrypt_password, verify_password
#Required for Flask-Security TRACKABLE
from werkzeug.contrib.fixers import ProxyFix
from flask_mail import Mail

# This is for SSE protocol
import gevent
from gevent import monkey
#from gevent.pywsgi import WSGIServer
monkey.patch_all()

app = Flask(__name__)
db = SQLAlchemy(app)


# The below jinja features are required to generate templates and remove whitespaces.
# If the below are enabled a service restart is required to show new HTML content edited in the file.
# However tests proved it does not need to be enabled a - & + next to jinja blocks does the trick.
#app.jinja_env.trim_blocks = True
#app.jinja_env.lstrip_blocks = True
app.config.from_object('config')
#Required for Flask-Security TRACKABLE
app.wsgi_app = ProxyFix(app.wsgi_app, num_proxies=1)
socketio = SocketIO(app)
#app._static_folder = os.path.abspath("static")

from iomate import iomate_global, models
from models import User, Role, Switch1_24_port, Switch2_24_port, Switch1_48_port, Switch2_48_port, Customer_sw, Firewall1_interfaces, Firewall2_interfaces

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
app.security = Security(app, user_datastore)
mail = Mail(app)

#@app.before_first_request
#def create_user():
#    db.create_all()
#    user_datastore.create_user(email='lo3k@hextrim.com', password=encrypt_password('lo3k'))
#    user_datastore.create_role(name='admin', description='Administrators')
##    user_datastore.create_user(email='test@hextrim.com', password=encrypt_password('test'))
##    user_datastore.create_role(name='superuser', description='Super User')
#    assign_role = user_datastore.find_role("admin")
##    assign_role = user_datastore.find_role("superuser")
#    assign_user = user_datastore.find_user(email='lo3k@hextrim.com')
##    assign_user = user_datastore.find_user(email='test@hextrim.com')
#    user_datastore.add_role_to_user(assign_user, assign_role)
#    user_datastore.add_role_to_user(assign_user, assign_role)
#    db.session.commit()
#    for i in range(1,25):
#        port_sw1_24 = Switch1_24_port('None', 'None', 'None', 'None', bool(False)) 
#        port_sw2_24 = Switch2_24_port('None', 'None', 'None', 'None', bool(False))
#        db.session.add(port_sw1_24)
#        db.session.add(port_sw2_24)
#        db.session.commit()
#    for i in range(1,49):
#        port_sw1_48 = Switch1_48_port('None', 'None', 'None', 'None', bool(False))
#        port_sw2_48 = Switch2_48_port('None', 'None', 'None', 'None', bool(False))
#        db.session.add(port_sw1_48)
#        db.session.add(port_sw2_48)
#        db.session.commit()
#    customer_sw_1 = Customer_sw('customer_sw_1', 'None', 'None', 'None')
#    customer_sw_2 = Customer_sw('customer_sw_2', 'None', 'None', 'None')
#    db.session.add(customer_sw_1)
#    db.session.add(customer_sw_2)
#    db.session.commit()
#    for i in range(1,9):
#        firewall1_interface = Firewall1_interfaces('None', 'None', 'None', 'None', bool(False), 'None', '')
#        firewall2_interface = Firewall2_interfaces('None', 'None', 'None', 'None', bool(False), 'None', '')
#        db.session.add(firewall1_interface)
#        db.session.add(firewall2_interface)
#        db.session.commit()


#Imports current_user from flask_security and via @app.context_processor return value of current_user into "user" and therefore "user" can be used in base.html in {% if user.has_role('') %} 
@app.context_processor
def inject_data():
    return dict(user=current_user)

db.create_all()
