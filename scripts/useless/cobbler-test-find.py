#!/usr/bin/env python

import re
import sys
import fileinput 

cobbler_config = open("/etc/cobbler/dhcp.template", "r")
for line in cobbler_config:
    subnet = re.search(r"\b(subnet)+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line)
    netmask = re.search(r"\b(netmask)+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line)
    routers = re.search(r"\b(routers)+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line)
    domain_name_servers = re.search(r"\b(domain-name-servers)+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line)
    subnet_mask = re.search(r"\b(subnet-mask)+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line)
    dynamic_bootp = re.search(r"\b(dynamic-bootp)+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line)
    if subnet:
        print format(subnet.group())
    if netmask:
        print format(netmask.group())
    if routers:
        print format(routers.group())
    if domain_name_servers:
        print format(domain_name_servers.group())
    if subnet_mask:
        print format(subnet_mask.group())
    if dynamic_bootp:
        print format(dynamic_bootp.group())


print("#####################")

file = open("/etc/cobbler/dhcp.template", "r")
lines = file.readlines()

for i in range(20, 45):
    print (lines[i])











#myfile = fileinput.FileInput("/etc/cobbler/dhcp.template", inplace=True)

#for line in myfile:
#    line = re.sub(r"(subnet)+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", "subnet 192.123.1.0 ", line.rstrip())
#    print(line)

#for line in myfile:
#    line = re.sub(r"(netmask)+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", "netmask 255.255.0.0 ", line.rstrip())
#    print(line)

#for line in myfile:
#    line = re.sub(r"(routers)+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", "routers 192.168.1.165;", line.rstrip())
#    print(line)

#for line in myfile:
#    line = re.sub(r"(domain-name-servers)+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", "domain-name-servers 192.168.1.165;", line.rstrip())
#    print(line)

#for line in myfile:
#    line = re.sub(r"(subnet-mask)+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", "subnet-mask 255.255.0.0;", line.rstrip())
#    print(line)

#for line in myfile:
#    line = re.sub(r"\b(dynamic-bootp)+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", "dynamic-bootp 192.168.1.150 192.168.1.160;", line.rstrip())
#    print(line)

def cobbler_config_replace(string, var):
    myfile = fileinput.FileInput("/etc/cobbler/dhcp.template", inplace=True)
    for line in myfile:
        line = re.sub(r"(" + string + ")+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", string + " " + var + " ", line.rstrip())
        print(line)

cobbler_config_replace("netmask", "215.123.11.0")
