import sys
import time
import serial
import pexpect
from pexpect_serial import SerialSpawn

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
# Press RETURN to get started.
ss.sendline('\r')
#Would you like to terminate autoinstall? [yes]:
ss.expect('.+yes*')
ss.sendline('\r')
time.sleep(1)
#Would you like to enter the initial configuration dialog? [yes/no]:
ss.expect('.+yes/no*')
print ss.before
ss.sendline('no\r')
ss.expect('>')
print ss.before
ss.logfile = sys.stdout
console.close()
#switch erased
