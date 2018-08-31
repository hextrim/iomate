import serial
import sys
import time
from serial import SerialException

conf_commands = sys.argv[1]
#conf_commands = "output/customer-sw-1-24-Fa.expect"

console = serial.Serial('/dev/ttyUSB0', baudrate=9600, parity="N", stopbits=1, bytesize=8, timeout=None)

def read_serial(console):
    data_bytes = console.inWaiting()
    if data_bytes:
        return console.read(data_bytes)
    else:
        return ""

def send_command(console, cmd=''):
    console.write(cmd + '\r')
    time.sleep(1)
    return read_serial(console)

send_command(console, cmd='terminal lenght 0')
with open("serial_switch_deploy.log","a+") as f:
    co = open(conf_commands, 'r')
    for i in co:
        f.write(send_command(console, cmd=i))
    co.close()
print "[OK]: Switch Configuration Deployed!"
