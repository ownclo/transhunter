from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

f = urlopen('http://google.ru/')
data = f.read()

soup = BeautifulSoup (data, fromEncoding="cp1251")
string = soup.prettify()

for item in soup.findAll(True):
    if item.string and item.name == 'a':
        print (item.string)
