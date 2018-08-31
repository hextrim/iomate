import ast
import urllib
import sys

if len(sys.argv) != 2:
  print "Please run the script with a Jenkins or Hudson url as the only argument\n Example : python BuildParser.py http://ci.jruby.org"
  sys.exit(1)

url = str(sys.argv[1])
print url

xml_input_no_filter = ast.literal_eval(urllib.urlopen(url + "/api/python?depth=1&tree=executor[progress]").read())

progress = xml_input_no_filter['executor']

print progress
print progress['progress']

