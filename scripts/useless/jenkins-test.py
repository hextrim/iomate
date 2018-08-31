import sys
import codecs
import jenkins

first = sys.argv[1]
second = sys.argv[2]

print first
print second

srvjenkins = jenkins.Jenkins('http://localhost:8080', username='iomate', password='e78ecc73d3925424e85268ad0f50d9f4')
srvjobs = srvjenkins.get_jobs()
print srvjobs
my_job = srvjenkins.get_job_config('deploy_sw_5')
print(my_job)
#    job = srvjenkins.get_jobs()
#if srvjobs['name'] == 'deploy_sw_5':
#    print "I got it"
#else:
#    print "Job does not exist"

match = any(d['name'] == 'deploy_sw_10' for d in srvjobs)

if match == True:
    print "Got IT!"
    config_xml = "output/config-sw-1-24-Fa.xml"
    with codecs.open(config_xml,'r',encoding='utf8') as f:
        config_xml_file = f.read()
        srvjenkins.reconfig_job('deploy_sw_10', config_xml_file)
        print "Reconfigured"
else:
    print "Where the fuck it is!"
    config_xml = "output/config-sw-1-24-Fa.xml"
    with codecs.open(config_xml,'r',encoding='utf8') as f:
        config_xml_file = f.read()
#                    srvjenkins.create_job('deploy_sw_2', 'config.xml')
        srvjenkins.create_job('deploy_sw_10', config_xml_file)
        print "Job created"



for l in srvjobs:
    if l['name'] == 'deploy_sw_5':
        print "I got it"
    else:
        print "Job does not exist"

#except:
#    print "DUPA"
job_inf = srvjenkins.get_job_info('deploy_sw_5')
print job_inf
print "#################"
last_build_number = srvjenkins.get_job_info('deploy_sw_5')['lastCompletedBuild']['number']
build_inf = srvjenkins.get_build_info('deploy_sw_5', last_build_number)
print build_inf

