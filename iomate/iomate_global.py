import serial
import time
from werkzeug.utils import secure_filename
from distutils.util import strtobool
from serial import SerialException
import jenkins
from jinja2 import Environment, FileSystemLoader
from iomate.iomate_app import app, render_template, request, db, flash, os, socketio, emit, url_for, copy_current_request_context, redirect, login_required, roles_required, encrypt_password, current_user, verify_password, SQLAlchemyUserDatastore, jsonify
from iomate.models import Racks, Servers, Routers, Firewalls, Ips, Switches, Subnets, Vlans, Vcenter, Esxis, VirtualMachines, Vsswitch, Vdsswitch, Vstorage, Isos, Snapshots, Templates, Sharedsan, Dedicatedsan, Nas, User, Role, Switch1_24_port, Switch2_24_port
from time import sleep
from threading import Thread, Event
from threading import Lock
#from flask_socketio import emit #SocketIO, emit
from random import random
import codecs
import gevent
import sys
import xmlrpclib
from xmlrpclib import *
import re
import fileinput
import ast
import urllib
from gevent import monkey
monkey.patch_all()

__author__ = 'lo3k@hextrim.com'

### GLOBAL VARIABLES ###
thread_connect_sw1 = None
thread_connect_sw2 = None
thread_deploy_sw_1_baseconfig_progressbar = None
thread_deploy_sw_1_portconfig_progressbar = None
thread_deploy_sw_1_singleport_progressbar = None
thread_livecd_build = None
thread_livecd_convert = None
thread_lock = Lock()


### JENKINS SERVER ###
srvjenkins = jenkins.Jenkins('http://localhost:8080', username='iomate', password='626002e8235dfc5c049f74ce2ef012ac')

### JENKINS ###
def get_deploy_device_running_build_progress(job, deviceprogressbar):
#def get_deploy_device_running_build_progress():
    while True:
        url = 'http://iomate:626002e8235dfc5c049f74ce2ef012ac@localhost:8080/job/' + job + '/lastBuild'
#        url = 'http://iomate:626002e8235dfc5c049f74ce2ef012ac@localhost:8080/job/deploy_sw_1/lastBuild'
        xml_input_no_filter = ast.literal_eval(urllib.urlopen(url + "/api/python?depth=1&tree=executor[progress]").read())
        progress = xml_input_no_filter['executor']
        if progress == None:
#            socketio.emit('sw1progressbar', {'data': '0'}, namespace='/swxprogress')
            socketio.emit(deviceprogressbar, {'data': '0'}, namespace='/swxprogress')
        else:
            progress_bar = progress['progress']
#            socketio.emit('sw1progressbar', {'data': progress_bar }, namespace='/swxprogress')
            socketio.emit(deviceprogressbar, {'data': progress_bar }, namespace='/swxprogress')

def get_build_item_running_build_progress():
    while True:
        url = 'http://iomate:626002e8235dfc5c049f74ce2ef012ac@localhost:8080/job/build_hextrimos_iso/lastBuild'
        xml_input_no_filter = ast.literal_eval(urllib.urlopen(url + "/api/python?depth=1&tree=executor[progress]").read())
        progress = xml_input_no_filter['executor']
        if progress == None:
            socketio.emit('build_hextrimos_iso_progressbar', {'data': '0'}, namespace='/livecdprogress')
        else:
            progress_bar = progress['progress']
            socketio.emit('build_hextrimos_iso_progressbar', {'data': progress_bar }, namespace='/livecdprogress')

def get_convert_item_running_build_progress():
    while True:
        url = 'http://iomate:626002e8235dfc5c049f74ce2ef012ac@localhost:8080/job/convert_hextrimos_to_pxeboot/lastBuild'
        xml_input_no_filter = ast.literal_eval(urllib.urlopen(url + "/api/python?depth=1&tree=executor[progress]").read())
        progress = xml_input_no_filter['executor']
        if progress == None:
            socketio.emit('convert_hextrimos_to_pxeboot_progressbar', {'data': '0'}, namespace='/livecdprogress')
        else:
            progress_bar = progress['progress']
            socketio.emit('convert_hextrimos_to_pxeboot_progressbar', {'data': progress_bar }, namespace='/livecdprogress')

def get_deploy_device_running_builds():
    running_builds = srvjenkins.get_running_builds()
    return running_builds

def get_deploy_device_get_job_info(job):
    try:
        job_info = srvjenkins.get_job_info(job)['firstBuild']
        if job_info == '' or job_info == 'None':
            print "NEVER BUILT"
        else:
#            lastbuild = get_deploy_device_last_build_number(job)
#           nextbuildbumber = get_deploy_device_next_build_number(job)
#            deploy_device_last_build_info = srvjenkins.get_build_info(job, lastbuild)
#            print deploy_device_last_build_info['result']
            return get_deploy_device_last_build_info(job)
    except:
        print "NEVER BUILT"
        return "NEVER BUILT"

def get_deploy_device_last_build_info(job):
    lastbuild = get_deploy_device_last_build_number(job)
    deploy_device_last_build_info = srvjenkins.get_build_info(job, lastbuild)
#    print deploy_device_last_build_info['result']
    return deploy_device_last_build_info['result']

def get_deploy_device_last_build_number(job):
    last_build_number = srvjenkins.get_job_info(job)['lastCompletedBuild']['number']
    return last_build_number

def get_deploy_device_next_build_number(job):
    next_build_number = srvjenkins.get_job_info(job)['nextBuildNumber']
    return next_build_number

def get_deploy_device_last_build_log(job):
    try:
        lastbuild = get_deploy_device_last_build_number(job)
        last_build_log = srvjenkins.get_build_console_output(job, lastbuild)
        return last_build_log
    except:
        return "NEVER BUILT - NO LOG"

### XML JENKINS JOBS ARE NOW DEPLOYED MANUALLY ###
#def build_jenkins_xml_sw(sw_config):
#    try:
#        if sw_config == 'baseconfig':
#            template_file = 'config-sw-1.j2'
#            template_output = "output/customer-sw-1-baseconfig.deploy"
#            template_xml = "output/config-sw-1-baseconfig.xml"
#        elif sw_config == 'portconfig':
#            template_file = 'config-sw-1.j2'
#            template_output = "output/customer-sw-1-portconfig.deploy"
#            template_xml = "output/config-sw-1-portconfig.xml"
#        elif int(sw_config) in range(1, 24):
### TODO
#            template_file = 'config-sw-1.j2'
#            template_output = "output/customer-sw-1-singleport.deploy"
#            template_xml = "output/config-sw-1-singleport.xml"
#        env = Environment(loader=FileSystemLoader(TEMPLATE_CONFIG_JENKINS))
#        template = env.get_template(template_file)
#        generate_template = template.render(customer_sw_1_deploy=template_output)
#        with open(template_xml, "wb") as f:
#            f.write(generate_template)
#	return True
#    except:
#        return False
#    else:
#        return False

### SERIAL FUNCTIONS ###
def cct_swx(serial_port, sw_usbevent, sw_portevent):
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
#    while True:
    try:
        console.open()
        if console.is_open is True:
            socketio.emit(sw_usbevent, {'data': 'CONNECTED'}, namespace='/swxprobe')
            print "Connected"
            gevent.sleep(1)
            time.sleep(1)
            try:
#                console.write('\r\n\r\n')
		console.write('\r\n')
                time.sleep(1)
                console_input = console.read(console.in_waiting)
                if console_input == '':
                    socketio.emit(sw_portevent, {'data': 'NOT READY&nbsp;'}, namespace='/swxprobe')
                    print "NOT READY"
                    console.close()
                    gevent.sleep(5)
                    time.sleep(5)
                elif console_input != '':
                    socketio.emit(sw_portevent, {'data': '&nbsp;&nbsp;&nbsp;&nbsp;READY&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'}, namespace='/swxprobe')
                    print "READY"
                    console.close()
                    gevent.sleep(1)
                    time.sleep(1)
            except serial.SerialException:
                socketio.emit(sw_portevent, {'data': '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LOST&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'}, namespace='/swxprobe')
                console.reset_input_buffer()
                console.close()
                gevent.sleep(2)
            except serial.SerialTimeoutException:
                socketio.emit(sw_portevent, {'data': '&nbsp;TIMEOUT&nbsp;'}, namespace='/swxprobe')
                console.reset_input_buffer()
                console.close()
                gevent.sleep(2)
            except:
                socketio.emit(sw_portevent, {'data': '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LOST&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'}, namespace='/swxprobe')
                print "LOST"
                console.reset_input_buffer()
                console.close()
                gevent.sleep(2)
        else:
            socketio.emit(sw_usbevent, {'data': 'NO SIGNAL'}, namespace='/swxprobe')
            print "No Signal"
            console.reset_input_buffer()
            console.close()
            gevent.sleep(2)
    except serial.SerialException:
        socketio.emit(sw_usbevent, {'data': '&nbsp;&nbsp;&nbsp;&nbsp;ERROR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'}, namespace='/swxprobe')
        print "Error"
        console.close()
        gevent.sleep(2)
    except:
        socketio.emit(sw_usbevent, {'data': '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LOST&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'}, namespace='/swxprobe')
        print "LOST"
        console.close()
        gevent.sleep(2)

### LOCAL CONFIG ###
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

OUTPUT = 'output'
OUTPUT_DIR = os.path.join(BASE_DIR, OUTPUT)

TEMPLATE_DIR = 'templates/configuration_templates/pyserial'
TEMPLATE_CONFIG = os.path.join(BASE_DIR, TEMPLATE_DIR)

TEMPLATE_DIR_JENKINS = '../jenkins/jobs'
TEMPLATE_CONFIG_JENKINS = os.path.join(BASE_DIR, TEMPLATE_DIR_JENKINS)

TEMPLATE_DIR_SALTSTACK = 'templates/configuration_templates/livecd'
TEMPLATE_CONFIG_SALTSTACK = os.path.join(BASE_DIR, TEMPLATE_DIR_SALTSTACK)

##### SOCKETIO #####

### SOCKETIO LIVECD ###
@socketio.on('connect', namespace='/livecdprogress')
def livecd_progress_connect():
    global thread_livecd_build
    with thread_lock:
        if thread_livecd_build is None:
            thread_livecd_build = socketio.start_background_task(target=get_build_item_running_build_progress)
    global thread_livecd_convert
    with thread_lock:
        if thread_livecd_convert is None:
            thread_livecd_convert = socketio.start_background_task(target=get_convert_item_running_build_progress)

@socketio.on('disconnect', namespace='/livecdprogress')
def livecd_progress_disconnect2():
    print "Disco"

### SOCKETIO SWITCH PROBE ###
@socketio.on('connect', namespace='/swxprobe')
def console_connect_sw():
    print "Connected"
#    global thread_connect_sw1
#    with thread_lock:
#        if thread_connect_sw1 is None:
#            thread_connect_sw1 = socketio.start_background_task(cct_swx, '/dev/ttyUSB0', 'sw1usbsignal', 'sw1portsignal')
#    global thread_connect_sw2
#    with thread_lock:
#        if thread_connect_sw2 is None:
#            thread_connect_sw2 = socketio.start_background_task(cct_swx, '/dev/ttyUSB1', 'sw2usbsignal', 'sw2portsignal')
#            thread_connect_sw2 = socketio.start_background_task(target=cct_sw2)

@socketio.on('disconnect', namespace='/swxprobe')
def console_disconnect_sw():
    print "Disco"

### SOCKETIO SWITCH PROGRESS ###
@socketio.on('connect', namespace='/swxprogress')
def progress_sw_connect():
    global thread_deploy_sw_1_baseconfig_progressbar
    global thread_deploy_sw_1_portconfig_progressbar
    global thread_deploy_sw_1_singleport_progressbar
    with thread_lock:
        if thread_deploy_sw_1_baseconfig_progressbar is None:
            thread_deploy_sw_1_baseconfig_progressbar = socketio.start_background_task(get_deploy_device_running_build_progress, 'deploy_sw_1_baseconfig', 'deploysw1-baseconfig-progress')
        if thread_deploy_sw_1_portconfig_progressbar is None:
            thread_deploy_sw_1_portconfig_progressbar = socketio.start_background_task(get_deploy_device_running_build_progress, 'deploy_sw_1_portconfig', 'deploysw1-portconfig-progress')
        if thread_deploy_sw_1_singleport_progressbar is None:
            thread_deploy_sw_1_singleport_progressbar = socketio.start_background_task(get_deploy_device_running_build_progress, 'deploy_sw_1_singleport', 'deploysw1-singleport-progress')
#            thread_deploy_progress_sw1 = socketio.start_background_task(get_deploy_device_running_build_progress, 'deploy_sw_2_baseconfig', 'deploysw2-baseconfig-progress')
#            thread_deploy_progress_sw1 = socketio.start_background_task(get_deploy_device_running_build_progress, 'deploy_sw_2_portconfig', 'deploysw2-portconfig-progress')
#            thread_deploy_progress_sw1 = socketio.start_background_task(get_deploy_device_running_build_progress, 'deploy_sw_2_singleport', 'deploysw2-singleport-progress')
#    print "Connected to progress"

@socketio.on('disconnect', namespace='/swxprogress')
def progress_sw_disconnect():
    print "Disco"

