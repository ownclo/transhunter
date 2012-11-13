#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#page = urlopen("http://habrahabr.ru/post/158385/")
with open ('article.html', 'r') as page:
    soup = BeautifulSoup(page.read())

id_pattern = re.compile("^comment_")
class_pattern = "message html_format "

for comment in soup.findAll (name = 'div',
                        attrs = {'class' : class_pattern}):
    print (comment.prettify())
