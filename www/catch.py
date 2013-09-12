#!/usr/bin/env python
import urllib
import urllib2
import re
nameRule = re.compile('<a\s*href=\'(?P<www>[^\']*)\'>(?P<name>.*?)</a>(?P<des>[^<]*)</td>')
contentRule = re.compile('<td\s*align=[^>]*>([^<]*)</td>')
paragraphRule = re.compile('<div class="cfp" align="left">(.*?)</div>', re.S)
#replace = re.compile('\n|\t|\r|<br>|\W')
fout = file("data.txt", 'w')
def getInformation(www):
    response = urllib2.urlopen(www)
    html = response.read()
    result = contentRule.findall(html)
    for i in result:
        fout.write(i + '\n')
    result = paragraphRule.search(html)
    result = result.group(1)#replace.sub(' ', result.group(1))
    #print result
    fout.write(result + '\n')
def getIndex(website, location):
    response = urllib2.urlopen(website + location)
    html = response.read()
    result = nameRule.findall(html)
    for i in result:
        print website + i[0]
        fout.write(website + i[0] + '\n')
        fout.write(i[1] + '\n')
        fout.write(i[2] + '\n')
        getInformation(website + urllib.quote(i[0], ";/?:@&=+$,") + '\n')
        fout.write("%%\n")
website = "http://www.wikicfp.com"
location = "/cfp/series?t=c&i=A"
getIndex(website, location)
fout.close()
