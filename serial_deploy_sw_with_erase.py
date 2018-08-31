import serial
import sys
import time
from serial import SerialException

conf_commands = sys.argv[1]
serial_port = sys.argv[2]
#erase_commands = ['\r\n','rancid','','enable','','write erase','\r','reload','\r']
erase_commands = ['rancid','','enable','','write erase','\r','reload','\r']


#console = serial.Serial('/dev/ttyUSB0', baudrate=9600, parity="N", stopbits=1, bytesize=8, timeout=None)

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

#send_command(console, cmd='terminal lenght 0')
#with open("serial_switch_deploy.log","a+") as f:
#    co = open(conf_commands, 'r')
#    for i in co:
#        f.write(send_command(console, cmd=i))
#    co.close()
#print "[OK]: Switch Configuration Deployed!"

#def erase_sw(serial_port):
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
    time.sleep(1)
    console_check = console.read(console.in_waiting)
    time.sleep(1)
#    console_check = console.readlines()
    if '>' in console_check:
        print console_check
        print '[INFO]: Found > prompt. Executing exit to jump to default console window.'
        console.write("exit")
	time.sleep(3)
    elif 'Press RETURN to get started.' or 'Would you like to terminate autoinstall? [yes]:' or 'Would you like to enter the initial configuration dialog? [yes/no]:' in console_check:
	print '[INFO]: Switch at Press RETURN to get started. or similar'
        break

console.flush()
console.reset_input_buffer()
console.reset_output_buffer()


time.sleep(2)
console.write("\r")
time.sleep(2)

#time.sleep(2)
#console.write("\r")
#time.sleep(1)
#console.write("\r")
#time.sleep(1)
data_buffer = console.read(console.in_waiting)
print data_buffer
if 'Username:' in data_buffer:
    print "[INFO]: Received Username in data buffer!"
    print "[INFO]: Proceeding with switch erase process!"
#    send_command(console, cmd='terminal lenght 0')
    try:
        with open("serial_switch_erase.log","a+") as f:
            for i in erase_commands:
                f.write(send_command(console, cmd=i))
        print "[OK]: Switch erased! Rebooting..."
        while True:
            checking = console.readline()
            print checking
            with open("serial_switch_reboot.log","a+") as e:
                for x in checking:
                    e.write(x)
            if 'Press RETURN to get started!' in checking:
                print "[INFO]: Switch reboot completed!"
                break
            else:
                print "[INFO]: Switch is rebooting..."

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
            print "[OK]: Switch erased and on > prompt!"
#        send_command(console, cmd='terminal lenght 0')
            with open("serial_switch_deploy.log","a+") as f:
                co = open(conf_commands, 'r')
                for i in co:
                    f.write(send_command(console, cmd=i))
                co.close()
            print "[OK]: Switch Configuration Deployed!"
            console.close()
        else:
            print "[ERROR]: Could not skip the default switch initial configuration procedure!"
            console.close()
            sys.exit(10)
    except:
        sys.exit(10)
#    console.close()
#    sys.exit(0)
#elif to if
elif 'Would you like to terminate autoinstall? [yes]:' or 'Would you like to enter the initial configuration dialog? [yes/no]:' or 'Switch>' in data_buffer:
    print "[INFO]: Received switch configuration defaults!"
    print "[INFO]: Proceeding with clean configuration..."
#    send_command(console, cmd='terminal lenght 0')
    try:
        with open("serial_switch_deploy.log","a+") as f:
            co = open(conf_commands, 'r')
            for i in co:
                f.write(send_command(console, cmd=i))
            co.close()
        print "[OK]: Switch configuration deployed!"
        console.close()
    except:
        sys.exit(10)
else:
#elif data_buffer == '':
    print "[ERROR]: Ups! Something went wrong!"
    console.close()
    sys.exit(10)

console.close()

