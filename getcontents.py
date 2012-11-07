from urllib2 import urlopen
from lxml.html import parse, open_in_browser, tostring

testfile = open ('test.html', 'w')
data = parse('http://google.com').getroot()
string = tostring(data, pretty_print=True)
testfile.write (string)
testfile.close ()
#for element in data.body.iter():
#    print ("%s --- %s" % (element.tag, element.text))
#print (datainfo.encoding)
