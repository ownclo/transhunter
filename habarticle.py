#!/usr/bin/python3
import sys
from os.path import isfile
from urllib.request import urlopen
from bs4 import BeautifulSoup
from operator import itemgetter
import re

class Reader:
    def __init__ (self, pageaddr):
        self.pageaddr = pageaddr
        self.page = self.read()

    def read (self):
        if self.pageaddr is sys.stdin:
            content = pageaddr.read()
        elif isfile(self.pageaddr):
                content = open (self.pageaddr, 'r').read()
        else:
            content = urlopen(self.pageaddr).read()
        return content

id_pattern = re.compile("^comment_")
adict = {'class':'comment_item', 'id':id_pattern}
topCommentsDict = {'class':'comments_list ', 'id':'comments'}

class Parser:
    def parse (content):
        return BeautifulSoup(content)

    def findComments (soup):
        return soup.findAll (name = 'div', attrs = adict)

    def get_content (comment):
        content = comment.find (name = 'div', attrs = adict)
        if not content: content = comment
        return content

    def get_score(comment):
        score_tag = comment.find (name = 'span', attrs = {'class' : 'score'})
        score_string = score_tag['title'].split(':')[0]
        score_num = int (score_string.split()[1])
        return score_num

    def prettyString (item):
        return item.prettify()

class Rater:
    def rate(soup):
        rated_comments = []
        for comment in Parser.findComments(soup):
            content = Parser.get_content (comment)
            score = Parser.get_score(comment)
            rated_comments.append({'comment' : content, 'score' : score})
        return rated_comments

    def sort(rated_comments):
        sorted_comments = sorted (rated_comments,
                                       key=itemgetter('score'),
                                       reverse = True)
        return sorted_comments

    def print_rates(sorted_comments):
        for item in sorted_comments:
            print (item['score'])

    def print_comments(sorted_comments):
        for item in sorted_comments:
            print (Parser.prettyString(item['comment']))

def main (pageaddr):
    page = Reader(pageaddr).page
    soup = Parser.parse(page)
    rated = Rater.rate (soup)
    sortd = Rater.sort (rated)
    Rater.print_rates (sortd)
    subtree = soup.find (name = 'div', attrs = topCommentsDict)

#page = urlopen("http://habrahabr.ru/post/158385/")
if __name__ == '__main__':
    if len(sys.argv) == 2:
        pageaddr = sys.argv[1]
    else:
        pageaddr = sys.stdin
    main (pageaddr)
