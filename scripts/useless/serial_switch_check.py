import serial
import sys
import time

#serial_port = sys.argv[1]

def erase_sw(serial_port):
    console = serial.Serial()
    console.port = serial_port
    console.baudrate = 9600
    console.parity = "N"
    console.stopbits = 1
    console.bytesize = 8
    console.timeout = 1
    console.dsrdtr = False
    console.rtscts = False
    console.xonxoff = False

    console.open()
    time.sleep(2)
    console.write("\r")
    time.sleep(1)
    console.write("\r")
    time.sleep(1)
    data_buffer = console.read(console.in_waiting)
    print data_buffer
    if 'Username:' in data_buffer:
        print "Username"
        console.close()
	sys.exit(0)
    elif 'Would you like to terminate autoinstall? [yes]:' or 'Would you like to enter the initial configuration dialog? [yes/no]:' or 'Switch>' in data_buffer:
        print "Switch>"
    else:
        print "Something Else"
    console.close()

erase_sw('/dev/ttyUSB0')
