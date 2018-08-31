import itertools

distros = [{'name': 'CentOS', 'arch': 'x86'}, {'name': 'HexOS', 'arch': 'x64'}, {'name': 'DupOS', 'arch': 'x32'}]

for it in distros:
#    for key in it.items():
#        value = key['name']
#	print value
    dupa = it.get('name')
    print dupa
