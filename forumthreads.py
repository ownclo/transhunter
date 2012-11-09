#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

with open('forumdisplay.php', 'r') as page:
    soup = BeautifulSoup(page.read())

for topic in soup.findAll(recursive = True,
                        attrs = {'id' : re.compile("^thread_title_")}):
        print ("%s -- %s" % (topic['href'], topic.string))
