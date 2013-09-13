#!/usr/bin/env python
fin = file('functions.txt', 'r')
import re
import math
a = re.compile('(\-?\d*)x\*\*2')
b = re.compile('(\-?\d*)x[^\*]')
c = re.compile('[^\*]([\+\-]?\d+)[^x]')
def toInt(string):
    if not string:
        return 1
    elif string == ' ':
        return 1
    elif string == '-':
        return -1
    else:
        return eval(string)
def listInt(slist):
    La = 0
    for x in slist:
        La += toInt(x)
    return La
delete = re.compile('\s*')
for line in fin:
    line = delete.sub('', line)
    print line
    lr = re.match('^([^=]*)=([^=]*)$', line)
    left = " " + lr.group(1) + " "
    right = " " + lr.group(2) + " "
    #print left, right
    la = a.findall(left)
    lb = b.findall(left)
    lc = c.findall(left)
    La = listInt(la)
    Lb = listInt(lb)
    Lc = listInt(lc)
    ra = a.findall(right)
    rb = b.findall(right)
    rc = c.findall(right)
    Ra = listInt(ra)
    Rb = listInt(rb)
    Rc = listInt(rc)
    print La, Lb, Lc
    print Ra, Rb, Rc
    A = La - Ra
    B = Lb - Rb
    C = Lc - Rc
    D = B ** 2 - 4 * A * C
    if D < 0:
        print "x1 = ", (-B-complex(0,1)*math.sqrt(-1*D))/(2*A), ",x2 = ", (-B+complex(0,1)*math.sqrt(-1*D))/(2*A)
    else:
        print "x1 = ", (-B-math.sqrt(D))/(2*A), ",x2 = ", (-B+math.sqrt(D))/(2*A)
