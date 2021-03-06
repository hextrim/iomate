import sys
import codecs
import jenkins
import ast
import urllib

srvjenkins = jenkins.Jenkins('http://localhost:8080', username='iomate', password='7bb49fc3412291658c66bfd8ffb219fb')

def get_deploy_device_running_build_progress(job):
    while True:
#   url = 'http://iomate:7bb49fc3412291658c66bfd8ffb219fb@localhost:8080/job/deploy_sw_1/lastBuild'
        url = 'http://iomate:7bb49fc3412291658c66bfd8ffb219fb@localhost:8080/job/' + job + '/lastBuild'
        if url != '':
            print url
        else:
            print "URL DOES NOT EXIST"
        xml_input_no_filter = ast.literal_eval(urllib.urlopen(url + "/api/python?depth=1&tree=executor[progress]").read())
        progress = xml_input_no_filter['executor']
        if progress == None:
            print progress
	    break
        else:
            progress_bar = progress['progress']
            print progress_bar
#    while True:
#    pass


def get_deploy_device_get_job_info(job):
    try:
        job_info = srvjenkins.get_job_info(job)['firstBuild']
        if job_info == '' or job_info == 'None':
	    print "NEVER BUILT"
        else:
#            lastbuild = get_deploy_device_last_build_number(job)
#	    nextbuildbumber = get_deploy_device_next_build_number(job)
#            deploy_device_last_build_info = srvjenkins.get_build_info(job, lastbuild)
#            print deploy_device_last_build_info['result']
	    return get_deploy_device_last_build_info(job)
    except:
        print "NEVER BUILT"
	return "NEVER BUILT"

def get_deploy_device_running_builds():
    running_builds = srvjenkins.get_running_builds()
    print running_builds
    return running_builds

def get_deploy_device_last_build_info(job):
    lastbuild = get_deploy_device_last_build_number(job)
    deploy_device_last_build_info = srvjenkins.get_build_info(job, lastbuild)
    print deploy_device_last_build_info['result']
    return deploy_device_last_build_info['result']

def get_deploy_device_last_build_number(job):
    last_build_number = srvjenkins.get_job_info(job)['lastCompletedBuild']['number']
    print last_build_number
    return last_build_number

def get_deploy_device_next_build_number(job):
    next_build_number = srvjenkins.get_job_info(job)['nextBuildNumber']
    print next_build_number
    return next_build_number


def get_deploy_device_last_build_log(job):
    try:
        lastbuild = get_deploy_device_last_build_number(job)
        last_build_log = srvjenkins.get_build_console_output(job, lastbuild)
        print last_build_log
        return last_build_log
    except:
	print "NEVER BUILT"
        return "NEVER BUILT - NO LOG"


get_deploy_device_get_job_info('deploy_sw_1')
#get_deploy_device_last_build_info('deploy_sw_1')
#get_deploy_device_last_build_number('deploy_sw_1')
#get_deploy_device_next_build_number('deploy_sw_10')
get_deploy_device_last_build_log('deploy_sw_10')
#get_deploy_device_running_builds()
#get_deploy_device_running_build_progress('deploy_sw_1')

#log = get_deploy_device_last_build_log('deploy_sw_1')
#print log

