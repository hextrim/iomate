import serial
import sys
import time
from serial import SerialException

#conf_commands = ['\r\n','rancid','','enable','','write erase','\r','reload','\r']
conf_commands = ['\r\n','rancid','','enable','','write erase','\r']

#console = serial.Serial('/dev/ttyUSB0', baudrate=9600, parity="N", stopbits=1, bytesize=8, timeout=None)

#console = serial.Serial()
#console.port = "/dev/ttyUSB0"

def checkusb(port):
    while True:
        try:
#           console = serial.Serial('/dev/ttyUSB0', baudrate=9600, parity="N", stopbits=1, bytesize=8, timeout=None)
           console = serial.Serial(port, baudrate=9600, parity="N", stopbits=1, bytesize=8, timeout=None)
            print "Connected"
            time.sleep(10)
##        break
        except serial.SerialException:
            print "Disconnected"
            time.sleep(10)

checkusb('/dev/ttyUSB0')
checkusb('/dev/ttyUSB1')
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




#if not console.isOpen():
#    return "<div>response</div>"
#    print "Console is closed!"
#    sys.exit()
#listen for flask input + POST mode/ajax
   

#def read_serial(console):
#    data_bytes = console.inWaiting()
#    if data_bytes:
#        return console.read(data_bytes)
#    else:
#        return ""

#def send_command(console, cmd=''):
#    console.write(cmd + '\r')
#    time.sleep(1)
#    return read_serial(console)

#send_command(console, cmd='terminal lenght 0')
#with open("erase_confirm.txt","a+") as f:
#    for i in conf_commands:
#        f.write(send_command(console, cmd=i))
