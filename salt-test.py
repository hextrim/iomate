#import salt.runner
import json
import salt.config
#master_opts = salt.config.client_config('/etc/salt/master')
import six

#import salt.loader
#opts = salt.config.minion_config('/etc/salt/master')
#grains = salt.loader.grains(opts)

import salt.client
local = salt.client.LocalClient()
key_ip = '192.168.1.26'
pxe_int_name = local.cmd(key_ip, 'network.ifacestartswith', [ key_ip ])
pxe_mac_addr = local.cmd(key_ip, 'network.hwaddr', [ pxe_int_name[key_ip][0] ])
print pxe_int_name[key_ip][0], pxe_mac_addr[key_ip]




#hwaddr = local.cmd('192.168.1.26', 'network.hwaddr', ['ens32'])
#hwaddr2 = local.cmd('192.168.1.82', 'network.hwaddr', ['ens160'])
#hwaddr3 = local.cmd('192.168.1.77', 'network.interfaces')

#print hwaddr
#print hwaddr2
#print hwaddr3
#for w in hwaddr3.keys():
#    print w

#specific_keys_from_a_range=list(hwaddr3.keys())
#print specific_keys_from_a_range

#for i, item, (interface, (e,f,g), (z,x,y), c) in enumerate(hwaddr3.iteritems()):
#for i in hwaddr3.iteritems():
##    print i
#    for m in i:
#        print m
#        for (n, l, k) in m:
#            print n
#            print l
#            print k
#    for a in item:
#        for m in interface:
#            find_mac = filter(lambda x : x['hwaddr'] == inteface, hwaddr3)
#            if find_mac:
#                print ('ESXi=' + find_mac[0]['hwaddr'])
#            else:
#                print ('ESXi=None')



import salt.wheel
opts = salt.config.master_config('/etc/salt/master')
wheel = salt.wheel.WheelClient(opts)

def keys_all():
    ret = wheel.cmd('key.list_all')
#    wheel.cmd('key.list_all')
    return ret


def keys_unacc():
    ret = wheel.cmd('key.list', ['unaccepted'])
#    wheel.cmd('key.list_all')
    return ret['minions_pre']

def keys_acc():
    ret = wheel.cmd('key.list', ['accepted'])
#    wheel.cmd('key.list_all')
    return ret['minions']

def keys_denied():
    ret = wheel.cmd('key.list', ['denied'])
#    wheel.cmd('key.list_all')
    return ret['minions_denied']

def keys_rej():
    ret = wheel.cmd('key.list', ['rejected'])
#    wheel.cmd('key.list_all')
    return ret['minions_rejected']

def salt_keys_denied():
    ret_denied = wheel.cmd('key.list', ['denied'])
#    if len(ret_denied['minions_denied']) == 0:
#        return None
#    else:
#    return ret_denied['minions_denied']
    print ret_denied['minions_denied']


#def showkeys():
#    shows = local.cmd('*', 'cmd.run', ['whoami'])
##    local.cmd('*', 'cmd.run', ['whoami'])
#    print shows
 
#salt_keys_denied()
#keys_all()
#keys_denied()
#keys_acc()
#keys_unacc()
#keys_rej()
#wheel.cmd('key.list_all')

#import os
#import os.path
#
#PATH='/var/run/salt-master.pid'
#
#if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print "File exists and is readable"
#else:
#    print "Either file is missing or is not readable"
