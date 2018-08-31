#!/usr/bin/python

import re
import sys
import xmlrpclib
from xmlrpclib import *


cobbler_server = xmlrpclib.Server("http://192.168.1.163/cobbler_api")
token = cobbler_server.login("cobbler", "cobbler")

#print cobbler_profile_name_find
#print '#######################'

#cobbler_profile_name_find = "Tue Apr 24 08:42:32 2018 - INFO | creating new distro: CentOS-7-Minimal-1708-x86_64"


#for lines in cobbler_profile_name_find:
##    result = re.sub("^.+distro: ", "" , lines)
#    result = re.search("^.+distro", lines, re.MULTILINE)
##    if result:
#        print result.group()

#print cobbler_profile_name_find

#cobbler_profile_name_find = cobbler_server.get_event_log("2018-04-25_161509_import")
#export = re.compile(r"distro:.*?\n", re.DOTALL|re.MULTILINE)
#outpost = export.search(cobbler_profile_name_find)
#result = re.sub("distro: ", "", outpost.group(0)).rstrip()
#
#print result

cobbler_task_name = "2018-04-25_161509_import"

def cobbler_os_name_find(cobbler_task_name):
    cobbler_distro_name_find = cobbler_server.get_event_log(cobbler_task_name)
    cobbler_distro_name_find_regex = re.compile(r"distro:.*?\n", re.DOTALL|re.MULTILINE)
    cobbler_distro_name_find_regex_match = cobbler_distro_name_find_regex.search(cobbler_distro_name_find)
    cobbler_distro_name_find_regex_substitute = re.sub("distro: ", "", cobbler_distro_name_find_regex_match.group(0)).rstrip()
    return cobbler_distro_name_find_regex_substitute

test = cobbler_os_name_find(cobbler_task_name)
print test
    




#fl = re.compile('(abc|def|ghi)')
#ts = 'xyz abc mno def'
#ms = fl.sub('zzz', ts)
#print ms  # xyz zzz mno zzzfl = re.compile('(abc|def|ghi)')



#result = re.search("distro", cobbler_profile_name_find, re.MULTILINE)
#if result:
#    print format(result.group())

#result = re.match(r'(.*) distro:(.*?) .*', cobbler_profile_name_find, re.M|re.I)
#if result:
#    print result

#for line in cobbler_profile_name_find:
#    if re.findall("distro", line):
#        print line
