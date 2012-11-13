#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
from operator import itemgetter
import re

def get_score(score_tag):
    score_string = score_tag['title'].split(':')[0]
    score_num = int (score_string.split()[1])
    return score_num

#page = urlopen("http://habrahabr.ru/post/158385/")
with open ('article.html', 'r') as page:
    soup = BeautifulSoup(page.read())

id_pattern = re.compile("^comment_")
adict = {'class':'comment_item', 'id':id_pattern}

rated_comments = []

for comment in soup.findAll (name = 'div', attrs = adict):
    score_tag = comment.find (name = 'span', attrs = {'class' : 'score'})
    score = get_score(score_tag)
    rated_comments.append({'comment' : comment, 'score' : score})

sorted_comments = sorted (rated_comments, reverse = True, key=itemgetter('score'))
for item in sorted_comments:
    print (item['score'])
#Haskell style:
#list (map (lambda x: print (x['score']), sorted_comments))
