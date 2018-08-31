import serial
import sys
import time
from serial import SerialException

conf_commands = sys.argv[1]
serial_port = sys.argv[2]
login_commands = ['rancid','','enable','','\r']

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

time.sleep(20)
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

console.close()

console.open()
console.flush()
console.reset_input_buffer()
console.reset_output_buffer()


while True:
    console.write("\r")
    time.sleep(2)
    console_check = console.read(console.in_waiting)
#    console_check = console.readlines()
    time.sleep(1)
    print '###CONSOLE CHECK###'
    print console_check
    print '###CONSOLE CHECK###'
    if 'Press RETURN to get started.' in console_check:
	print '[INFO]: Switch at Press RETURN to get started. or similar'
        break
    elif '#' in console_check:
        print console_check
        print '[INFO]: Found # prompt. Executing exit to jump to default console window.'
        console.write("exit")
        time.sleep(3)
    elif '>' in console_check:
        print console_check
        print '[INFO]: Found > prompt. Executing exit to jump to default console window.'
        console.write("exit")
        time.sleep(3)
    elif 'Would you like to terminate autoinstall? [yes]:' in console_check:
        print console_check
        print '[ERROR]: Switch at default factory boot settings.'
        console.close()
        sys.exit(10)
    elif 'Would you like to enter the initial configuration dialog? [yes/no]:' in console_check:
        print console_check
        print '[ERROR]: Switch at default factory boot settings.'
        console.close()
        sys.exit(10)

console.flush()
console.reset_input_buffer()
console.reset_output_buffer()

time.sleep(2)
console.write("\r")
time.sleep(2)

data_buffer = console.read(console.in_waiting)
print data_buffer
if 'Username:' in data_buffer:
    print "[INFO]: Received Username in data buffer!"
    print "[INFO]: Proceeding with switch portconfig deployment!"
#    send_command(console, cmd='terminal lenght 0')
    try:
        with open("serial_switch_portconfig.log","a+") as f:
            for i in login_commands:
                f.write(send_command(console, cmd=i))
        print "[OK]: Login commands sent!"

        console.write("\r\n")
        time.sleep(1)
        data_buffer = console.read(console.in_waiting)
        if '#' in data_buffer:
	    print data_buffer
            print "[OK]: Logged in and on # prompt!"
            with open("serial_switch_deploy.log","a+") as f:
                co = open(conf_commands, 'r')
                for i in co:
                    f.write(send_command(console, cmd=i))
                co.close()
            print "[OK]: Switch port configuration deployed!"
            console.close()
        else:
            print data_buffer
            print "[ERROR]: Could not log in!"
            console.close()
            sys.exit(10)
    except:
        print "[ERROR]: Ups! Something went wrong!"
        console.close()
        sys.exit(10)

elif 'Would you like to terminate autoinstall? [yes]:' or 'Would you like to enter the initial configuration dialog? [yes/no]:' or 'Switch>' in data_buffer:
    print '[ERROR]: Switch at default factory boot settings!!!!!.'
    console.close()
    sys.exit(10)
else:
    print "[ERROR]: Ups! Something went wrong!!!!!"
    console.close()
    sys.exit(10)

console.close()
