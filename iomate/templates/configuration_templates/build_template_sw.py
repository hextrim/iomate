from jinja2 import Environment, FileSystemLoader
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def build_template_sw1():
    env = Environment(loader=FileSystemLoader(THIS_DIR))
    template = env.get_template('customer-sw-1-48.j2')
    generate_template = template.render(customer='HEXTRIM', customer_sw_2='ht-sw-2', customer_sw_1='ht-sw-1', customer_fw_1='ht-fw-1', mgmt_vlan_id='10', vmotion_vlan_id='20', iscsi_vlan_id='30', outside_vlan_id='40', customer_defined_vlan='50', customer_esxi_1='ht-esxi-1', customer_esxi_2='ht-esxi-2', customer_esxi_3='ht-esxi-3', customer_esxi_4='ht-esxi-4', customer_esxi_5='ht-esxi-5', customer_esxi_6='ht-esxi-6', customer_sw_1_mgmt_ipadress='192.168.1.101', customer_sw_1_mgmt_subnet='255.255.255.0', customer_sw_1_mgmt_gateway='192.168.1.254', customer_san_1='ht-san-01')

    print generate_template
    with open("customer-sw-1-48.deploy", "wb") as f:
        f.write(generate_template)

def build_template_sw2():
    env = Environment(loader=FileSystemLoader(THIS_DIR))
    template = env.get_template('customer-sw-2-48.j2')
    generate_template = template.render(customer='HEXTRIM', customer_sw_1='ht-sw-1', customer_sw_2='ht-sw-2', customer_fw_2='ht-fw-2', mgmt_vlan_id='10', vmotion_vlan_id='20', iscsi_vlan_id='30', outside_vlan_id='40', customer_defined_vlan='50', customer_esxi_1='ht-esxi-1', customer_esxi_2='ht-esxi-2', customer_esxi_3='ht-esxi-3', customer_esxi_4='ht-esxi-4', customer_esxi_5='ht-esxi-5', customer_esxi_6='ht-esxi-6', customer_sw_2_mgmt_ipadress='192.168.1.102', customer_sw_1_mgmt_subnet='255.255.255.0', customer_sw_1_mgmt_gateway='192.168.1.254', customer_san_2='ht-san-02')

    print generate_template
    with open("customer-sw-2-48.deploy", "wb") as f:
        f.write(generate_template)



if __name__ == '__main__':
    build_template_sw1()
    build_template_sw2()

! killall minicom