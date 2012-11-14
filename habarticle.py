#!/usr/bin/python3
from os.path import isfile
from urllib.request import urlopen
from bs4 import BeautifulSoup
from operator import itemgetter
import re

class Parser:
    def __init__ (self, pageaddr):
        self.pageaddr = pageaddr
        self.page = self.parse()

    def parse (self):
        if isfile(self.pageaddr):
            content = open (self.pageaddr, 'r')
        else:
            content = urlopen(self.pageaddr)
        soup = BeautifulSoup(content.read())
        return soup

class Rater:
    def __init__ (self, soup):
        self.rated_comments = []
        self.soup = soup

    def rate(self):
        id_pattern = re.compile("^comment_")
        adict = {'class':'comment_item', 'id':id_pattern}

        for comment in self.soup.findAll (name = 'div', attrs = adict):
            score_tag = comment.find (name = 'span', attrs = {'class' : 'score'})
            score = self.get_score(score_tag)
            self.rated_comments.append({'comment' : comment, 'score' : score})
        return self

    def sort(self):
        self.sorted_comments = sorted (self.rated_comments, reverse = True, key=itemgetter('score'))

    def get_score(self, score_tag):
        score_string = score_tag['title'].split(':')[0]
        score_num = int (score_string.split()[1])
        return score_num

    def print_rates(self):
        for item in self.sorted_comments:
            print (item['score'])

def main (pageaddr):
    soup = Parser(pageaddr).page
    sortd = Rater(soup)
    sortd.rate().sort()
    sortd.print_rates()

#page = urlopen("http://habrahabr.ru/post/158385/")
if __name__ == '__main__':
    main ('article.html')
