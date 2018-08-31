import os
import cobbler.api as capi
import sys

cobbler_api = capi.BootAPI()

listimages = cobbler_api.images()
listprofiles = cobbler_api.profiles()
listsystems = cobbler_api.systems()

for p in listprofiles:
    print p.name
box = listprofiles.find(name="*",return_list=True)
for d in box:
    print d.name

#!/usr/bin/python

#import re
#import sys
#import xmlrpclib
#from xmlrpclib import *

#system_name="ht-esxi-test"
#new_name="ht-esxi-api"


#conn = ServerProxy("http://192.168.1.163/cobbler_api")
#cobbler_server = xmlrpclib.Server("http://192.168.1.163/cobbler_api")

#token = conn.login("cobbler","cobbler")
#token = cobbler_server.login("cobbler", "cobbler")

#something = cobbler_server.get_events()
#list_of_distros = cobbler_server.get_profiles()
#for i in list_of_distros:
##    dupa = i["name"]
#    dupa = i
#    print dupa

#profile = "VMware-VMvisor-Installer-5.5.0-1331820-x86_64"
#something = cobbler_server.remove_distro(profile, token)
#cobbler_server.sync(token)


#cobbler_server.logout(token)

