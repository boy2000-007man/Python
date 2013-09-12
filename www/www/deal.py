#!/usr/bin/env python
import re
wordSplit = re.compile('\s*')
replace = re.compile('\n|\t|\r|<br>|\W|_')

fin = file('data.txt', 'r')
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
        if line == '%%\n':
            break
        words += wordSplit.split(replace.sub(' ', line.lower()))
    tmp = set(words)
    totalWord.append(tmp)
    global wordSet
    wordSet |= tmp
    return tmp
while process():
    pass
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
from django.shortcuts import render_to_response
index = """<title>Supervisor Search Engine</title>
    <form method="GET" action="/search">
    Words:<input type="text" name="word">
    <input type="submit" name="submit">
    </form>"""
notfound = """<title>Not Found</title>
    Click <a href="/search">here</a> to go back."""
@csrf_exempt
def search(request):
    if not request.GET.has_key('submit'):
        return HttpResponse(index)
    words = wordSplit.split(str(request.GET['word']).lower())
    res = set(dic[''])
    for word in words:
        if not dic.has_key(word):
            res = list()
            break
        res &= set(dic[word])
    if not res:
        return HttpResponse(notfound)
    tmp = list()
    for x in res:
        tmp.append(URL[x])
    return render_to_response('res.html', {'result' : tmp})
