#!/usr/bin/env python
import urllib
import urllib2
import re
nameRule = re.compile('<a\s*href=\'(?P<www>[^\']*)\'>(?P<name>.*?)</a>(?P<des>[^<]*)</td>')
contentRule = re.compile('<td\s*align=[^>]*>([^<]*)</td>', re.M)
paragraphRule = re.compile('<div class="cfp" align="left">[\n\t\s]*(.*?)[\n\t\s]*</div>', re.S)
#replace = re.compile('\n|\t|\r|<br>|\W')
fout = file("data.txt", 'w')
def getInformation(www):
    response = urllib2.urlopen(www)
    html = response.read()
    result = contentRule.findall(html)
    for i in result:
        fout.write(i + '\n')
    fout.write("%%\n")
    result = paragraphRule.search(html)
    result = result.group(1)#replace.sub(' ', result.group(1))
    #print repr(result)
    fout.write(result + '\n')
    fout.write("%%\n")
num = 0
def getIndex(website, location):
    response = urllib2.urlopen(website + location)
    html = response.read()
    result = nameRule.findall(html)
    for i in result:
        global num
        num = num + 1
        if num == 185:
            continue
        print num, website + i[0]
        fout.write(website + i[0] + '\n')
        fout.write(i[1] + '\n')
        fout.write(i[2] + '\n')
        getInformation(website + urllib.quote(i[0], ";/?:@&=+$,") + '\n')
        if num == 201:
            break
website = "http://www.wikicfp.com"
location = "/cfp/series?t=c&i="
for i in ['A', 'B', 'C']:
    getIndex(website, location + i)
fout.close()
