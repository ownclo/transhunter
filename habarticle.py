#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#page = urlopen("http://habrahabr.ru/post/158385/")
with open ('article.html', 'r') as page:
    soup = BeautifulSoup(page.read())

id_pattern = re.compile("^comment_")
adict = {'class':'comment_item', 'id':id_pattern}

for comment in soup.findAll (name = 'div', attrs = adict):
    score = comment.find (name = 'span', attrs = {'class' : 'score'})
    print (score.string)
