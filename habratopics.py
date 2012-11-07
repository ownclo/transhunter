#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen("http://habrahabr.ru/")
soup = BeautifulSoup(page.read())

for topic in soup.findAll(True, 'post_title'):
    print ("%s -- %s" % (topic['href'], topic.contents[0]))
