#!/usr/bin/env python
import re
name = re.compile('<td\s*class="[^"]*">([^<\(\)]*)</td>[^<]*<td[^>]*>([^<]*)</td>', re.M)
fin = file('tsinghuaprecident.html', 'r')
content = fin.read()
fin.close()
fout = file('rst.txt', 'w')
names = name.findall(content)
for x in names:
    tmp = list(x)
    print tmp[0], tmp[1]
    fout.write(tmp[0] + '      ' + tmp[1] + '\n')
fout.close()
