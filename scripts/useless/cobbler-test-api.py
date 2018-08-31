#import os
#import cobbler.api as capi
#import sys

#cobbler_api = capi.BootAPI()

#listimages = cobbler_api.images()
#listprofiles = cobbler_api.profiles()
#listsystems = cobbler_api.systems()

#for p in listprofiles:
#    print "dupa %s" % (listprofiles,)
#print format(str(listprofiles))
#box = listsystems.find('ht-esxi-test')
#print box

#!/usr/bin/python

import re
import sys
import xmlrpclib
from xmlrpclib import *

system_name="ht-esxi-test"
new_name="ht-esxi-api"


#conn = ServerProxy("http://192.168.1.163/cobbler_api")
cobbler_server = xmlrpclib.Server("http://192.168.1.163/cobbler_api")

#token = conn.login("cobbler","cobbler")
token = cobbler_server.login("cobbler", "cobbler")

# Check for systems and create if it doesn't exist
#try:
#    sys_id = conn.get_system_handle(system_name, token)
#except Fault, reason:
#    if reason.faultCode == 1:
#        sys_id = conn.new_system(token)
#        pass
#    else:
#        raise
##sys_id = conn.get_system_handle(system_name, token)
##print sys_id
##conn.rename_system(sys_id, new_name, token)
##sys_id = conn.get_system_handle(new_name, token)
##print sys_id
##conn.save_system(sys_id, token)
#cobbler_server.background_import({ "path" : "/mnt", "arch" : "x86_64", "name" : "CentOS-6.7-x86_64-minimal" }, token)
#something = cobbler_server.get_task_status("2018-04-24_081345_import")
#something = cobbler_server.get_event_log("2018-04-24_081345_import")
#something = cobbler_server.get_event_log("2018-04-24_084216_import")
#something = cobbler_server.get_events()
#print something


(year, month, day, hour, minute, second, weekday, julian, dst) = time.localtime()
iso_import_date = "%04d-%02d-%02d_%02d%02d" % (year,month,day,hour,minute)
print iso_import_date
def cobbler_import(import_iso_date):
    while True:
        something = cobbler_server.get_events()
        for event in something:
#        r = re.compile("2018-04-11_1719.*")
            r = re.compile("" + import_iso_date  + ".*")
            event = filter(r.match, something)
        print event[0]
        event_result = cobbler_server.get_task_status(event[0])
        print event_result[2]
        if event_result[2] == 'complete':
            break
    return event_result[2], event[0]

#def cobbler_import_taskname(import_iso_date):
#    while True:
#        something = cobbler_server.get_events()
#        for event in something:
##        r = re.compile("2018-04-11_1719.*")
#            r = re.compile("" + import_iso_date  + ".*")
#            event = filter(r.match, something)
#        print event[0]
#	break
#    return event[0]

#cobbler_import_taskname(iso_import_date)


output1, output2 = cobbler_import(iso_import_date)
#if cobbler_import(iso_import_date) == 'complete':
#    print "CONFIRMED"
if output1 == 'complete':
    print "CONFIRMED"
print '######'
print output2
cobbler_server.logout(token)


#timefloat = float(time.time())
#print timefloat

#filename = "CentOS-6.7-x86_64-minimal.iso"
#filename = "VMware-VMvisor-Installer-6.0.0.update02-3620759.x86_64.iso"
#filesplit = filename.rsplit('.', 1)
#print filesplit[0]
