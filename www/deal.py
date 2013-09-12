#!/usr/bin/env python
import re
wordSplit = re.compile('\s*')
replace = re.compile('\n|\t|\r|<br>|\W|_')

fin = file("data.txt", 'r')
totalWord = list()
wordSet = set()
URL = list()

def process():
    dic = {}
    line = fin.readline()
    if not line:
        return None
    dic['url'] = line
    line = fin.readline()
    dic['title'] = line
    line = fin.readline()
    dic['sub'] = line
    URL.append(dic)
    words = wordSplit.split(replace.sub(' ', dic['title'].lower())) + wordSplit.split(replace.sub(' ', dic['sub'].lower()))
    while 1:
        line = fin.readline()
        if line == "%%\n":
            break
        words += wordSplit.split(replace.sub(' ', line.lower()))
    tmp = set(words)
    totalWord.append(tmp)
    global wordSet
    wordSet |= tmp
    return tmp
while process():
    pass
fout = file("res.txt", "w")
dic = {}
for x in wordSet:
    i = 0
    tmp = list()
    for w in totalWord:
        if x in w:
            tmp.append(i)
        i = i + 1
    dic[x] = tmp
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
index = """<title>Supervisor Search Engine</title>
    <form method="GET" action="/search">
    Word:<input type="text" name="word">
    <input type="submit"/>
    </form>"""
@csrf_exempt
def search(request):
    if not request.word:
        return HttpResponse(index)
    word = word.lower()
    if not dic.has_key(word):
        return None
    tmp = list()
    for x in dic[word]:
        tmp.append(URL[x])
    return tmp
