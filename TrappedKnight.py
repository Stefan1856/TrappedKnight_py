#!/usr/bin/python
import Feld
import Sort
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def tK(startx,starty,Bewegung1,Bewegung2,maxitt):
    startpos = (startx , starty , Feld.wert(startx,starty))
    b = (Bewegung1,Bewegung2)

    Besucht = tuple([startpos])
    Besuchtx = [startpos[0]]
    Besuchty = [startpos[1]]
    Besuchtwert = [startpos[2]]

    pos = startpos
    frei = True

    i = 0
    while((i < maxitt)and(frei)):
        frei = False
        i = i+1
        #mögliche nächste Positionen
        möglpos=[( pos[0]+b[0] , pos[1]+b[1] , Feld.wert(pos[0]+b[0],pos[1]+b[1]) ),
                 ( pos[0]+b[0] , pos[1]-b[1] , Feld.wert(pos[0]+b[0],pos[1]-b[1]) ),
                 ( pos[0]-b[0] , pos[1]+b[1] , Feld.wert(pos[0]-b[0],pos[1]+b[1]) ),
                 ( pos[0]-b[0] , pos[1]-b[1] , Feld.wert(pos[0]-b[0],pos[1]-b[1]) ),
                 ( pos[0]+b[1] , pos[1]+b[0] , Feld.wert(pos[0]+b[1],pos[1]+b[0]) ),
                 ( pos[0]+b[1] , pos[1]-b[0] , Feld.wert(pos[0]+b[1],pos[1]-b[0]) ),
                 ( pos[0]-b[1] , pos[1]+b[0] , Feld.wert(pos[0]-b[1],pos[1]+b[0]) ),
                 ( pos[0]-b[1] , pos[1]-b[0] , Feld.wert(pos[0]-b[1],pos[1]-b[0]) )]

        Sort.BubbleList(möglpos)

        for j in möglpos:
            if(not (j in Besucht)):
                pos = j
                Besucht = Besucht + tuple([j])
                Besuchtx = Besuchtx + [j[0]]
                Besuchty = Besuchty + [j[1]]
                Besuchtwert = Besuchtwert + [j[2]]
                frei = True
                break
    return [Besucht , Besuchtx , Besuchty , Besuchtwert , [pos , i]]


def trKnight(x,y,b1,b2,maxitt):
    return tK(x,y,b1,b2,maxitt)[0]

def trKnightx(x,y,b1,b2,maxitt):
    return tK(x,y,b1,b2,maxitt)[1]

def trKnighty(x,y,b1,b2,maxitt):
    return tK(x,y,b1,b2,maxitt)[2]

def trKnightwert(x,y,b1,b2,maxitt):
    return tK(x,y,b1,b2,maxitt)[3]

def trKnightend(x,y,b1,b2,maxitt):
    return tK(x,y,b1,b2,maxitt)[4]


def plotKnight(x,y,b1,b2,maxitt):
    X     = trKnightx  (x,y , b1,b2 , maxitt)
    Y     = trKnighty  (x,y , b1,b2 , maxitt)
    pos   = trKnightend(x,y , b1,b2 , maxitt)[0]
    steps = trKnightend(x,y , b1,b2 , maxitt)[1]

    plt.plot(pos[0] , pos[1] ,'ro:', MarkerSize=3)
    plt.plot(X , Y, 'k', '_', linewidth=0.5)
    plt.plot(0 , 0 ,'ro:', MarkerSize=3)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('trapped knight: endpos:' + str(pos) +'Schritte:' + str(steps))
    plt.show()

def plotKnightx(x,y,b1,b2,maxitt):
    X = trKnightx  (x,y , b1,b2 , maxitt)
    r = list(range(len(X)))

    plt.plot(r , X, 'k', '_', linewidth=0.5)
    plt.xlabel('Schritte')
    plt.ylabel('x')
    plt.title('trapped knight')
    plt.show()

def plotKnighty(x,y,b1,b2,maxitt):
    Y = trKnighty  (x,y , b1,b2 , maxitt)
    r = list(range(len(Y)))

    plt.plot(r , Y, 'k', '_', linewidth=0.5)
    plt.xlabel('Schritte')
    plt.ylabel('y')
    plt.title('trapped knight')
    plt.show()

def plotKnightwert(x,y,b1,b2,maxitt):
    W = trKnightwert  (x,y , b1,b2 , maxitt)
    r = list(range(len(W)))

    plt.plot(r , W, 'k', '_', linewidth=0.5)
    plt.xlabel('Schritte')
    plt.ylabel('Wert')
    plt.title('trapped knight')
    plt.show()
