#!/usr/bin/env python
import re
wordSplit = re.compile('\s*')
replace = re.compile('\n|\t|\r|<br>|\W|_')

fin = file("data.txt", 'r')
totalWord = list()
wordSet = set()

def process():
    if not fin.readline():
        return None
    words = list()
    while 1:
        line = fin.readline()
        if line == "%%\n":
            break
        words += wordSplit.split(replace.sub(' ', line))
    tmp = set(words)
    totalWord.append(tmp)
    global wordSet
    wordSet |= tmp
    #print wordSet
    return tmp
while process():
    pass
#print totalWord
#print wordSet
print wordSet
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
def search(word):
    if not dic.has_key(word):
        return None
    return dic[word]
