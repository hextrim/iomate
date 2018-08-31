import serial
import sys
import time
from serial import SerialException
import pexpect
from pexpect_serial import SerialSpawn

conf_commands = ['\r\n','rancid','','enable','','write erase','\r','reload','\r']
#conf_commands = "output/customer-sw-1-24-Fa.expect"

console = serial.Serial('/dev/ttyUSB0', baudrate=9600, parity="N", stopbits=1, bytesize=8, timeout=None)

#try:   
#    console = serial.Serial('/dev/ttyUSB0', baudrate=9600, parity="N", stopbits=1, bytesize=8, timeout=None)
#except serial.SerialException:
#    print "errot no serial open: "

#if console.isOpen():
#    try:
#       #input = console.read(console.inWaiting())
#       print "Dupa"
#    except serial.SerialException:
#        print "error to comm: "
#
#else:
#    print "cannot open port"

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
with open("erase_confirm2.txt","a+") as f:
    for i in conf_commands:
        f.write(send_command(console, cmd=i))


time.sleep(120)
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
