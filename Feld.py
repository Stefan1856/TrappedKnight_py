#!/usr/bin/python
import math

def wert(x,y):
    X = math.fabs(x)
    Y = math.fabs(y)
    n = int(((2*max([X,Y]))+1)**2)

    if(X>=Y):
        if(x>0):
            m = n-(5*X)+y
        else:
            m = n-X-y
    else:
        if(y>=0):
            m = n-(3*Y)-x
        else:
            m = n-(7*Y)+x
    return int(m)
