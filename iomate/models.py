from iomate.iomate_app import db, UserMixin, RoleMixin

## Flask-Security
roles_users = db.Table('roles_users', db.Column('user_id', db.Integer(), db.ForeignKey('user.id')), db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
#        return '<Role %r>' % (self.name)
        return str('%s').replace('[','').replace(']','') % (self.name)



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    profile_pic = db.Column(db.String(100))
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def __init__(self, email=None, username=None, password=None, last_login_at=None, current_login_at=None, last_login_ip=None, current_login_ip=None, login_count=None, active=None, confirmed_at=None, profile_pic=None, roles=None):
        self.email = email
        self.username = username
	self.password = password
	self.last_login_at = last_login_at
	self.current_login_at = current_login_at
	self.last_login_ip = last_login_ip
	self.current_login_ip = current_login_ip
	self.login_count = login_count
	self.active = active
	self.confirmed_at = confirmed_at
	self.profile_pic = profile_pic
	self.roles = roles

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def set_password():
        pass

    def check_password():
        pass

    def __repr__(self):
        return '<User %r>' % (self.username)
###

#class Users(db.Model):
#    __tablename__ = 'users'
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(50), unique=True)
#    email = db.Column(db.String(120), unique=True)
#
#    def __init__(self, name=None, email=None):
#        self.name = name
#        self.email = email
#
#    def __repr__(self):
#        return '<Users %r>' % (self.name)
#
#    def is_email_address_valid(email):
#        if not re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", email):
#            return False
#        return True


class Racks(db.Model):
    __tablename__ = 'racks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    location = db.Column(db.String(20))

    def __init__(self, name=None, location=None):
        self.name = name
        self.location = location

    def __repr__(self):
        return '<Racks %r>' % (self.name)

class Servers(db.Model):
    __tablename__ = 'servers'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(50), unique=True)
    ipaddress = db.Column(db.String(50), unique=True)
    subnet = db.Column(db.String(50))
    gateway = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    
    def __init__(self, hostname=None, ipaddress=None, subnet=None, gateway=None, username=None, password=None):
	self.hostname = hostname
	self.ipaddress = ipaddress
	self.subnet = subnet
	self.gateway = gateway
	self.username = username
	self.password = password

    def __repr__(self):
        return '%s' % (self.hostname)

class Routers(db.Model):
    __tablename__ = 'routers'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(50), unique=True)
    ipaddress = db.Column(db.String(50), unique=True)
    subnet = db.Column(db.String(50))
    gateway = db.Column(db.String(50))
    mgmtport = db.Column(db.String(50))
 
    def __init__(self, hostname=None, ipaddress=None, subnet=None, gateway=None, mgmtport=None):
        self.hostname = hostname
        self.ipaddress = ipaddress
        self.subnet = subnet
        self.gateway = gateway
        self.mgmtport = mgmtport

    def __repr__(self):
        return '<Routers %r>' % (self.hostname)

class Switches(db.Model):
    __tablename__ = 'switches'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(50), unique=True)
    ipaddress = db.Column(db.String(50), unique=True)
    subnet = db.Column(db.String(50))
    gateway = db.Column(db.String(50))
    mgmtvlan = db.Column(db.String(50))
    portnr = db.Column(db.String(2))
    porttype = db.Column(db.String(15))
    customer_sw = db.relationship('Customer_sw', backref='customerswbackref', lazy='dynamic')

    def __init__(self, hostname=None, ipaddress=None, subnet=None, gateway=None, mgmtvlan=None, portnr=None, porttype=None ):
        self.hostname = hostname
        self.ipaddress = ipaddress
        self.subnet = subnet
        self.gateway = gateway
        self.mgmtvlan = mgmtvlan
	self.portnr = portnr
	self.porttype = porttype

    def __repr__(self):
        return '<Switches %r>' % (self.hostname)

class Firewalls(db.Model):
    __tablename__ = 'firewalls'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(50), unique=True)
    ipaddress = db.Column(db.String(50), unique=True)
    subnet = db.Column(db.String(50))
    gateway = db.Column(db.String(50))
    mgmtnetwork = db.Column(db.String(50), unique=True)
    mgmtsubnet = db.Column(db.String(50))

    def __init__(self, hostname=None, ipaddress=None, subnet=None, gateway=None, mgmtnetwork=None, mgmtsubnet=None):
        self.hostname = hostname
        self.ipaddress = ipaddress
	self.subnet = subnet
	self.gateway = gateway
	self.mgmtnetwork = mgmtnetwork
	self.mgmtsubnet = mgmtsubnet

    def __repr__(self):
        return '<Firewalls %r>' % (self.hostname)

class Ips(db.Model):
    __tablename__ = 'ips'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(50), unique=True)
    ipaddress = db.Column(db.String(50), unique=True)
    subnet = db.Column(db.String(50))
    gateway = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self,hostname=None, ipaddress=None, subnet=None, gateway=None, username=None, password=None):
        self.hostname = hostname
        self.ipaddress = ipaddress
        self.subnet = subnet
        self.gateway = gateway
        self.username = username
        self.password = password

    def __repr__(self):
        return '<Ips %r>' % (self.hostname)

class Subnets(db.Model):
    __tablename__ = 'subnets'
    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(50), unique=True)
    name = db.Column(db.Integer, db.ForeignKey('vlans.id'))
    network = db.Column(db.String(50), unique=True)
    mask = db.Column(db.String(50))


    def __init__(self, name=None, network=None, mask=None):
	self.name = name
        self.network = network
        self.mask = mask

    def __repr__(self):
        return '<Subnets %r>' % (self.name)

class Vlans(db.Model):
    __tablename__ = 'vlans'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    vlanid = db.Column(db.String(50), unique=True)
    switch1_24_ports = db.relationship('Switch1_24_port', backref='sw124vlansbackref', lazy='dynamic')
    switch2_24_ports = db.relationship('Switch2_24_port', backref='sw224vlansbackref', lazy='dynamic')
    switch1_48_ports = db.relationship('Switch1_48_port', backref='sw148vlansbackref', lazy='dynamic')
    switch2_48_ports = db.relationship('Switch1_48_port', backref='sw248vlansbackref', lazy='dynamic')
    subnets = db.relationship('Subnets', backref='subnetsvlansbackref', lazy='dynamic')

    def __init__(self, name=None, vlanid=None):
        self.name = name
        self.vlanid = vlanid

    def __repr__(self):
        return '<Vlans %r>' % (self.name)

class Sharedsan(db.Model):
    __tablename__ = 'sharedsan'
    id = db.Column(db.Integer, primary_key=True)
    lunname = db.Column(db.String(50), unique=True)
    lunsize = db.Column(db.String(50))

    def __init__(self, lunname=None, lunsize=None):
        self.lunname = lunname
        self.lunsize = lunsize

    def __repr__(self):
        return '<Sharedsan %r>' % (self.lunname)

class Dedicatedsan(db.Model):
    __tablename__ = 'dedicatedsan'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(50), unique=True)
    ipaddress = db.Column(db.String(50))
    subnet = db.Column(db.String(50))
    gateway = db.Column(db.String(50))
    port = db.Column(db.String(50))
    provider = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, hostname=None, ipaddress=None, subnet=None, gateway=None, port=None, provider=None, username=None, password=None):
        self.hostname = hostname
        self.ipaddress = ipaddress
        self.subnet = subnet
        self.gateway = gateway
        self.port = port
        self.provider = provider
        self.username = username
        self.password = password


    def __repr__(self):
        return '<Dedicatedsan %r>' % (self.hostname)

class Nas(db.Model):
    __tablename__ = 'nas'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(50), unique=True)
    ipaddress = db.Column(db.String(50), unique=True)
    subnet = db.Column(db.String(50))
    gateway = db.Column(db.String(50))
    port = db.Column(db.String(50))
    provider = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, hostname=None, ipaddress=None, subnet=None, gateway=None, port=None, provider=None,  username=None, password=None):
        self.hostname = hostname
	self.ipaddress = ipaddress
        self.subnet = subnet
        self.gateway = gateway
        self.port = port
        self.provider = provider
        self.username = username
        self.password = password

    def __repr__(self):
        return '<Nas %r>' % (self.hostname)

class Vcenter(db.Model):
    __tablename__ = 'vcenter'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(50), unique=True)
    ipaddress = db.Column(db.String(50), unique=True)
    subnet = db.Column(db.String(50), unique=True)
    gateway = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50), unique=True)

    def __init__(self, hostname=None, ipaddress=None, subnet=None, gateway=None, username=None, password=None):
        self.hostname = hostname
	self.ipaddress = ipaddress
        self.subnet = subnet
        self.gateway = gateway
	self.username = username
	self.password = password

    def __repr__(self):
        return '<Vcenter %r>' % (self.hostname)

class Esxis(db.Model):
    __tablename__ = 'esxi'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(50), unique=True)
    ipaddress = db.Column(db.String(50), unique=True)
    subnet = db.Column(db.String(50))
    gateway = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, hostname=None, ipaddress=None, subnet=None, gateway=None, username=None, password=None):
        self.hostname = hostname
        self.ipaddress = ipaddress
        self.subnet = subnet
        self.gateway = gateway
        self.username = username
        self.password = password

    def __repr__(self):
        return '%s' % (self.hostname)

class VirtualMachines(db.Model):
    __tablename__ = 'virtualmachines'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(50), unique=True)
    ipaddress = db.Column(db.String(50), unique=True)
    subnet = db.Column(db.String(50))
    gateway = db.Column(db.String(50))
    portgroup = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, hostname=None, ipaddress=None, subnet=None, gateway=None, portgroup=None, username=None, password=None):
        self.hostname = hostname
        self.ipaddress = ipaddress
	self.subnet = subnet
        self.gateway = gateway
        self.portgroup = portgroup
        self.username = username
        self.password = password

    def __repr__(self):
        return '%s' % (self.hostname)

class Vsswitch(db.Model):
    __tablename__ = 'vsswitch'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    ipaddress = db.Column(db.String(50), unique=True)
    subnet = db.Column(db.String(50))
    gateway = db.Column(db.String(50))
    nic1 = db.Column(db.String(50), unique=True)
    nic2 = db.Column(db.String(50), unique=True)

    def __init__(self, name=None, ipaddress=None, subnet=None, gateway=None, nic1=None, nic2=None):
        self.name = name
        self.ipaddress = ipaddress
        self.subnet = subnet
        self.gateway = gateway
        self.nic1 = nic1
        self.nic2 = nic2

    def __repr__(self):
        return '<Vdsswitch %r>' % (self.name)


class Vdsswitch(db.Model):
    __tablename__ = 'vdsswitch'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    nic1 = db.Column(db.String(50))
    nic2 = db.Column(db.String(50))
    datacenter = db.Column(db.String(50))
    portgroup = db.Column(db.String(50), unique=True)
    portgroupvlan = db.Column(db.String(50), unique=True)

    def __init__(self, name=None, nic1=None, nic2=None, datacenter=None, portgroup=None, portgroupvlan=None):
        self.name = name
        self.nic1 = nic1
        self.nic2 = nic2
        self.datacenter = datacenter
        self.portgroup = portgroup
        self.portgroupvlan = portgroupvlan

    def __repr__(self):
        return '<Vdsswitch %r>' % (self.name)

class Vstorage(db.Model):
    __tablename__ = 'vstorage'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Vstorage %r>' % (self.name)

class Snapshots(db.Model):
    __tablename__ = 'snapshots'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    path = db.Column(db.String(50), unique=True)

    def __init__(self, name=None, path=None):
        self.name = name
        self.path = path

    def __repr__(self):
        return '<Snapshots %r>' % (self.name)

class Isos(db.Model):
    __tablename__ = 'isos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    filepath = db.Column(db.String(100), unique=True)
    filename = db.Column(db.String(80), unique=True)
    cobbler_status = db.Column(db.String(80))
    cobbler_name = db.Column(db.String(80))
    import_eventid = db.Column(db.String(80))

    def __init__(self, name=None, filename=None, filepath=None, cobbler_status=None, cobbler_name=None , import_eventid=None):
        self.name = name
	self.filename = filename
        self.filepath = filepath
	self.cobbler_status = cobbler_status
	self.cobbler_name = cobbler_name
        self.import_eventid = import_eventid

    def __repr__(self):
        return '<Isos %r>' % (self.name)

class Templates(db.Model):
    __tablename__ = 'templates'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    path = db.Column(db.String(50))

    def __init__(self, name=None, path=None):
        self.name = name
        self.path = path

    def __repr__(self):
        return '<Templates %r>' % (self.name)


class Firewall1_interfaces(db.Model):
    __tablename__ = 'firewall1_interfaces'
    id = db.Column(db.Integer, primary_key=True)
    vlan = db.Column(db.String(20))
    name = db.Column(db.String(20))
    seclvl = db.Column(db.String(10))
    subnet = db.Column(db.String(10))
    enabled = db.Column(db.Boolean())
    mode = db.Column(db.String(10))
    group = db.Column(db.Integer, db.ForeignKey('port_channels_fw1.id'))

    def __init__(self, vlan=None, name=None, seclvl=None, subnet=None, enabled=None, mode=None, group=None):
	self.vlan = vlan
        self.name = name
        self.seclvl = seclvl
        self.subnet = subnet
        self.enabled = enabled
        self.mode = mode
        self.group = group

    def __repr__(self):
        return '%r' % (self.id)

class Firewall2_interfaces(db.Model):
    __tablename__ = 'firewall2_interfaces'
    id = db.Column(db.Integer, primary_key=True)
    vlan = db.Column(db.String(20))
    name = db.Column(db.String(20))
    seclvl = db.Column(db.String(10))
    subnet = db.Column(db.String(10))
    enabled = db.Column(db.Boolean())
    mode = db.Column(db.String(10))
    group = db.Column(db.String(10))
#    group = db.Column(db.Integer, db.ForeignKey('port_channels.id'))

    def __init__(self, vlan=None, name=None, seclvl=None, subnet=None, enabled=None, mode=None, group=None):
        self.vlan = vlan
        self.name = name
        self.seclvl = seclvl
        self.subnet = subnet
        self.enabled = enabled
        self.mode = mode
        self.group = group

    def __repr__(self):
        return '%r' % (self.id)

class Port_channels_fw1(db.Model):
    __tablename__ = 'port_channels_fw1'
    id = db.Column(db.Integer, primary_key=True)
    vlan = db.Column(db.String(20))
    name = db.Column(db.String(20))
    seclvl = db.Column(db.String(10))
    subnet = db.Column(db.String(10))
    enabled = db.Column(db.Boolean())
    mode = db.Column(db.String(10))
#    group = db.Column(db.String(10))
    interfaces = db.relationship('Firewall1_interfaces', backref='interfaces', lazy='dynamic')

    def __init__(self, vlan=None, name=None, seclvl=None, subnet=None, enabled=None, mode=None, group=None):
        self.vlan = vlan
        self.name = name
        self.seclvl = seclvl
        self.subnet = subnet
        self.enabled = enabled
        self.mode = mode
        self.group = group

    def __repr__(self):
        return '%r' % (self.id)



class Switch1_24_port(db.Model):
    __tablename__ = 'switch1_24_port'
    id = db.Column(db.Integer, primary_key=True)
    devicename = db.Column(db.String(50))
    deviceport = db.Column(db.String(20))
    portmode = db.Column(db.String(10))
    portvlan = db.Column(db.String(10))
    portpxeboot = db.Column(db.Boolean())
    vlan_id = db.Column(db.Integer, db.ForeignKey('vlans.id'))
    
    def __init__(self, devicename=None, deviceport=None, portmode=None, portvlan=None, portpxeboot=None):
        self.devicename = devicename
        self.deviceport = deviceport
	self.portmode = portmode
	self.portvlan = portvlan
	self.portpxeboot = portpxeboot

    def __repr__(self):
        return '%r' % (self.id)

class Switch2_24_port(db.Model):
    __tablename__ = 'switch2_24_port'
    id = db.Column(db.Integer, primary_key=True)
    devicename = db.Column(db.String(50))
    deviceport = db.Column(db.String(20))
    portmode = db.Column(db.String(10))
    portvlan = db.Column(db.String(10))
    portpxeboot = db.Column(db.Boolean())
    vlan_id = db.Column(db.Integer, db.ForeignKey('vlans.id'))

    def __init__(self, devicename=None, deviceport=None, portmode=None, portvlan=None, portpxeboot=None):
        self.devicename = devicename
        self.deviceport = deviceport
        self.portmode = portmode
        self.portvlan = portvlan
        self.portpxeboot = portpxeboot

    def __repr__(self):
        return '<port %r>' % (self.id)

class Switch1_48_port(db.Model):
    __tablename__ = 'switch1_48_port'
    id = db.Column(db.Integer, primary_key=True)
    devicename = db.Column(db.String(50))
    deviceport = db.Column(db.String(20))
    portmode = db.Column(db.String(10))
    portvlan = db.Column(db.String(10))
    portpxeboot = db.Column(db.Boolean())
    vlan_id = db.Column(db.Integer, db.ForeignKey('vlans.id'))

    def __init__(self, devicename=None, deviceport=None, portmode=None, portvlan=None, portpxeboot=None):
        self.devicename = devicename
        self.deviceport = deviceport
        self.portmode = portmode
        self.portvlan = portvlan
        self.portpxeboot = portpxeboot

    def __repr__(self):
        return '<port %r>' % (self.id)

class Switch2_48_port(db.Model):
    __tablename__ = 'switch2_48_port'
    id = db.Column(db.Integer, primary_key=True)
    devicename = db.Column(db.String(50))
    deviceport = db.Column(db.String(20))
    portmode = db.Column(db.String(10))
    portvlan = db.Column(db.String(10))
    portpxeboot = db.Column(db.Boolean())
    vlan_id = db.Column(db.Integer, db.ForeignKey('vlans.id'))

    def __init__(self, devicename=None, deviceport=None, portmode=None, portvlan=None, portpxeboot=None):
        self.devicename = devicename
        self.deviceport = deviceport
        self.portmode = portmode
        self.portvlan = portvlan
        self.portpxeboot = portpxeboot

    def __repr__(self):
        return '<port %r>' % (self.id)

class Customer_sw(db.Model):
    __tablename__ = 'customer_sw'
    id = db.Column(db.Integer, primary_key=True)
    selfname = db.Column(db.String(15))
    baseconfig = db.Column(db.String(10))
    portconfig = db.Column(db.String(10))
    singleport = db.Column(db.String(10))
    switch_id = db.Column(db.Integer, db.ForeignKey('switches.id'))

    def __init__(self, selfname=None, baseconfig=None, portconfig=None, singleport=None):
        self.selfname = selfname
        self.baseconfig = baseconfig
        self.portconfig = portconfig
        self.singleport = singleport

    def __repr__(self):
        return '<Customer_sw %r>' % (self.selfname)

class Saltstack_pxe_nodes(db.Model):
    __tablename__ = 'saltstack_pxe_nodes'
    id = db.Column(db.Integer, primary_key=True)
    pxeipaddr = db.Column(db.String(15), unique=True)
    pxeint = db.Column(db.String(10))
    pxemac = db.Column(db.String(20))
    pxeinstalled = db.Column(db.Boolean())
#    vm_mac = db.relationship('System_vm_profiles', backref='systemvmbackref', lazy='dynamic')
    system_id = db.Column(db.Integer, db.ForeignKey('system_vm_profiles.id'))
    def __init__(self, pxeipaddr=None, pxeint=None, pxemac=None, pxeinstalled=None):
        self.pxeipaddr = pxeipaddr
        self.pxeint = pxeint
        self.pxemac = pxemac
	self.pxeinstalled = pxeinstalled

    def __repr__(self):
        return str('%s') % (self.pxeipaddr)


class System_phy_profiles(db.Model):
    __tablename__ = 'system_phy_profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True)
    mac = db.Column(db.String(10))

    def __init__(self, name=None, mac=None):
        self.name = name
        self.mac = mac

    def __repr__(self):
        return str('%s') % (self.mac)

class System_vm_profiles(db.Model):
    __tablename__ = 'system_vm_profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True)
    mac = db.Column(db.String(10))
#    salt_mac = db.Column(db.Integer, db.ForeignKey('saltstack_pxe_nodes.id'))
    salt_id = db.relationship('Saltstack_pxe_nodes', backref='saltvmbackref', lazy='dynamic')

#    def __init__(self, name=None, mac=None):
    def __init__(self, name=None, mac=None):
        self.name = name
        self.mac = mac

    def __repr__(self):
        return str('%s') % (self.name)


