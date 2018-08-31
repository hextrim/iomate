import sys
import time
import serial
import pexpect
from pexpect_serial import SerialSpawn

#serial_port = sys.argv[1]

conf_commands = ['\r','rancid\r','\r','enable\r\n','\r\n']

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
for i in conf_commands:
    ss.writelines(conf_commands)
#    time.sleep(1)
console.close()
#switch erased
