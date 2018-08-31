import napalm
from napalm import get_network_driver
driver = get_network_driver('ios')
optional_args = {'secret': ''}
device = driver('192.168.50.101', 'rancid', '', '280', optional_args=optional_args)
device.open()
mac_audit_sw1 = device.get_mac_address_table()
cisco_24_Fa = ['Fa0/1', 'Fa0/9', 'Fa0/13']
cisco_48_Fa = ['Fa0/5', 'Fa0/9', 'Fa0/13', 'Fa0/17', 'Fa0/21', 'Fa0/25']
cisco_24_Gi = ['Gi1/0/5', 'Gi1/0/9', 'Gi1/0/13']
cisco_48_Gi = ['Gi1/0/5', 'Gi1/0/9', 'Gi1/0/13', 'Gi1/0/17', 'Gi1/0/21', 'Gi1/0/25']
key = 0
for i, item in enumerate(cisco_24_Fa):
#for i in cisco_24_Fa:
    key += 1
    find_mac = filter(lambda x : x['interface'] == item, mac_audit_sw1)
#    find_mac = filter(lambda x : x['interface'] == i, mac_audit_sw1)
    if find_mac:
        print ('ESXi-' + str(key) + '=' + find_mac[0]['mac'])
    else:
        print ('ESXi-' + str(key) + '=None')
        

