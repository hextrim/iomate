import codecs
filename = 'config-sw-1-24-Fa.xml'
filename2 = 'config-sw-1-24-Fa2.xml'
with codecs.open(filename,'r',encoding='utf8') as f:
    text = f.read()
# process Unicode text
with codecs.open(filename2,'w',encoding='utf8') as f:
    f.write(text)
