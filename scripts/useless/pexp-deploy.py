import sys
import time
import serial
import pexpect
from pexpect_serial import SerialSpawn

conf_commands = "output/customer-sw-1-24-Fa.expect"

console = serial.Serial()
console.port = "/dev/ttyUSB0"
#console.port = serial_port
console.baudrate = 9600
console.parity = "N"
console.stopbits = 1
console.bytesize = 8
console.timeout = 1
console.dsrdtr = False
console.rtscts = False
console.xonxoff = False

console.open()
ss = SerialSpawn(console)
f = open(conf_commands, 'r')
for i in f:
    ss.writelines(f)
    time.sleep(2)
f.close()
console.close()
#switch erased
