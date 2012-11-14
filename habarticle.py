#!/usr/bin/python3
from os.path import isfile
from urllib.request import urlopen
from bs4 import BeautifulSoup
from operator import itemgetter
import re

def parse (page):
    if isfile(page):
        content = open (page, 'r')
    else:
        content = urlopen(page)
    soup = BeautifulSoup(content.read())
    return soup

def get_score(score_tag):
    score_string = score_tag['title'].split(':')[0]
    score_num = int (score_string.split()[1])
    return score_num

def rateComments (soup):
    id_pattern = re.compile("^comment_")
    adict = {'class':'comment_item', 'id':id_pattern}
    rated_comments = []

    for comment in soup.findAll (name = 'div', attrs = adict):
        score_tag = comment.find (name = 'span', attrs = {'class' : 'score'})
        score = get_score(score_tag)
        rated_comments.append({'comment' : comment, 'score' : score})
    return rated_comments

def sortComments (rated_comments):
    sorted_comments = sorted (rated_comments, reverse = True, key=itemgetter('score'))
    return sorted_comments

def print_rates (sorted_comments):
    for item in sorted_comments:
        print (item['score'])

def main (page):
    soup = parse (page)
    rated_comments = rateComments (soup)
    sorted_comments = sortComments (rated_comments)
    print_rates(sorted_comments)

#page = urlopen("http://habrahabr.ru/post/158385/")
if __name__ == '__main__':
    main ('article.html')
