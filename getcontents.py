#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup

f = urlopen('http://google.ru/')
data = f.read()

soup = BeautifulSoup (data, from_encoding="cp1251")
string = soup.prettify()

for item in soup.findAll(True):
    if item.string and item.name == 'a':
        print (item.string)
