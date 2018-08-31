#from iomate.iomate_app import app, db, socketio
from iomate.iomate_app import app
## BLUEPRINTS IMPORT
from iomate.dashboard import dashboard
from iomate.racks import racks
from iomate.servers import servers
from iomate.routers import routers
from iomate.firewalls import firewalls
from iomate.ips import ips
from iomate.subnets import subnets
from iomate.vlans import vlans
from iomate.sharedsan import sharedsan
from iomate.dedicatedsan import dedicatedsan
from iomate.nas import nas
from iomate.vcenter import vcenter
from iomate.esxi import esxi
from iomate.virtualmachines import virtualmachines
from iomate.vswitch import vswitch
from iomate.vdsswitch import vdsswitch
from iomate.vstorage import vstorage
from iomate.snapshots import snapshots
from iomate.templates import templates
from iomate.profile import profile
from iomate.users import users
from iomate.switches import switches
from iomate.isos import isos
from iomate.cobblered import cobblered
from iomate.design_sw1_24 import design_sw1_24
from iomate.design_sw2_24 import design_sw2_24
from iomate.design_fw1 import design_fw1
from iomate.livecd import livecd
from iomate.deploy_switch import deploy_switch
from iomate.statistics import statistics
from iomate.automation import automation
from iomate.saltstack import saltstack
#from iomate.system_profiles import system_profiles
from iomate.system_vm_profiles import system_vm_profiles
from iomate.system_phy_profiles import system_phy_profiles
from iomate.deploy_phy_system import deploy_phy_system
from iomate.deploy_vm_system import deploy_vm_system

## BLUEPRINTS REGISTER
app.register_blueprint(dashboard)
app.register_blueprint(racks)
app.register_blueprint(servers)
app.register_blueprint(routers)
app.register_blueprint(firewalls)
app.register_blueprint(ips)
app.register_blueprint(subnets)
app.register_blueprint(vlans)
app.register_blueprint(sharedsan)
app.register_blueprint(dedicatedsan)
app.register_blueprint(nas)
app.register_blueprint(vcenter)
app.register_blueprint(esxi)
app.register_blueprint(virtualmachines)
app.register_blueprint(vswitch)
app.register_blueprint(vdsswitch)
app.register_blueprint(vstorage)
app.register_blueprint(snapshots)
app.register_blueprint(templates)
app.register_blueprint(profile)
app.register_blueprint(users)
app.register_blueprint(switches)
app.register_blueprint(isos)
app.register_blueprint(cobblered)
app.register_blueprint(design_sw1_24)
app.register_blueprint(design_sw2_24)
app.register_blueprint(design_fw1)
app.register_blueprint(livecd)
app.register_blueprint(deploy_switch)
app.register_blueprint(statistics)
app.register_blueprint(automation)
app.register_blueprint(saltstack)
#app.register_blueprint(system_profiles)
app.register_blueprint(system_vm_profiles)
app.register_blueprint(system_phy_profiles)
app.register_blueprint(deploy_phy_system)
app.register_blueprint(deploy_vm_system)

## IOMATE MAIN APP START
if __name__ == "__main__":
    app.run(debug = True)
#No longer required
#    socketio.run(app, debug=True)

# This is for SSE protocol
#    http_server = WSGIServer(('127.0.0.1', 8000), app)
#    http_server.serve_forever()
