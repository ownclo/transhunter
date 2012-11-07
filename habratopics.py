from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

page = urlopen("http://habrahabr.ru/")
soup = BeautifulSoup(page.read())

for topic in soup.findAll(True, 'post_title'):
    print ("%s -- %s" % (topic['href'], topic.contents[0]))
