import serial
import sys
import time
from serial import SerialException

#console = serial.Serial('/dev/ttyUSB0', baudrate=9600, parity="N", stopbits=1, bytesize=8, timeout=None)

console = serial.Serial()
console.port = "/dev/ttyUSB0"
console.baudrate = 9600
console.parity = "N"
console.stopbits = 1
console.bytesize = 8
console.timeout = 1
console.dsrdtr = False
console.rtscts = False
console.xonxoff = False

console.close()
