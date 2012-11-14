#!/usr/bin/python3
import sys
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
        if self.pageaddr is sys.stdin:
            content = pageaddr.read()
        elif isfile(self.pageaddr):
                content = open (self.pageaddr, 'r').read()
        else:
            content = urlopen(self.pageaddr).read()
        soup = BeautifulSoup(content)
        return soup

class Rater:
    def __init__ (self, soup):
        self.rated_comments = []
        self.soup = soup
        id_pattern = re.compile("^comment_")
        self.adict = {'class':'comment_item', 'id':id_pattern}

    def rate(self):
        for comment in self.soup.findAll (name = 'div', attrs = self.adict):
            content = self.get_content (comment)
            score = self.get_score(comment)
            self.rated_comments.append({'comment' : content, 'score' : score})
        return self

    def sort(self):
        self.sorted_comments = sorted (self.rated_comments,
                                       key=itemgetter('score'),
                                       reverse = True)

    def get_content (self, comment):
        content = comment.find (name = 'div', attrs = self.adict)
        if not content: content = comment

    def get_score(self, comment):
        score_tag = comment.find (name = 'span', attrs = {'class' : 'score'})
        score_string = score_tag['title'].split(':')[0]
        score_num = int (score_string.split()[1])
        return score_num

    def print_rates(self):
        for item in self.sorted_comments:
            print (item['score'])

    def print_comments(self):
        for item in self.sorted_comments:
            print (item['comment'].prettify())


def main (pageaddr):
    soup = Parser(pageaddr).page
    sortd = Rater(soup)
    sortd.rate().sort()
    sortd.print_rates()

#page = urlopen("http://habrahabr.ru/post/158385/")
if __name__ == '__main__':
    if len(sys.argv) == 2:
        pageaddr = sys.argv[1]
    else:
        pageaddr = sys.stdin
    main (pageaddr)
