#!/usr/bin/env python
import re
wordSplit = re.compile('\s+')
replace = re.compile('\n|\t|\r|<br>|\W|_')
endline = re.compile('\r<br>')

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
    words = wordSplit.split(replace.sub(' ', dic['title'].lower())) + wordSplit.split(replace.sub(' ', dic['sub'].lower()))
    while 1:
        line = fin.readline()
        if line == '%%\n':
            break
        words += wordSplit.split(replace.sub(' ', line.lower()))
    line = fin.readline()
    dic['content'] = endline.split(line)
    #print dic['content']
    URL.append(dic)
    words += wordSplit.split(replace.sub(' ', line.lower()))
    fin.readline()
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
    Words:<input type="text" name="words">
    <input type="submit" name="submit">
    </form>"""
@csrf_exempt
def search(request):
    if not request.GET.has_key('submit'):
        return HttpResponse(index)
    words = wordSplit.split(str(request.GET['words']).lower())
    res = set(dic[''])
    for word in words:
        if not dic.has_key(word):
            res = list()
            break
        res &= set(dic[word])
    tmp = list()
    for x in res:
        URL[x]['find'] = list()
        for t in URL[x]['content']:
            z = ' '+t+' '
            k = False
            for word in words:
                if re.search('\W'+word+'\W', ' '+t+' ', re.I):
                    k = True
                    j = re.compile(word, re.I)
                    z = j.sub('<font color=red>'+word+'</font>', z)
            if k:
                URL[x]['find'].append(z)
        tmp.append(URL[x])
    return render_to_response('res.html', {'result': tmp, 'number': len(tmp), 'words': str(request.GET['words'])})
