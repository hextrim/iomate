import serial
import sys
import time
from serial import SerialException

conf_commands = ['\r\n','rancid','','enable','','write erase','\r','reload','\r']

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
with open("serial_switch_erase.log","a+") as f:
    for i in conf_commands:
        f.write(send_command(console, cmd=i))

print "[OK] Switch Erased! Rebooting..."

while True:
    checking = console.readline()
    print checking
    with open("serial_switch_reboot.log","a+") as e:
        for x in checking:
            e.write(x)
    if 'Press RETURN to get started!' in checking:
        print "Completed"
        break
    else:
        print "Not yet"

console.write("\r")
data_buffer = console.read(console.in_waiting)
if 'Would you like to terminate autoinstall? [yes]:' in data_buffer:
    console.write("\r\r")
time.sleep(2)
console.write("\r\n")
time.sleep(5)
console.write("\r\n")
time.sleep(1)
data_buffer = console.read(console.in_waiting)
if 'Would you like to enter the initial configuration dialog? [yes/no]:' in data_buffer:
    console.write("no\r")
time.sleep(1)
data_buffer = console.read(console.in_waiting)
if 'Switch>' in data_buffer:
    print "[OK]: Switch Erased and on > prompt!"
else:
    print "[ERROR]: Could not skip the default switch initial configuration procedure!"
