# -*- coding: utf-8 -*-
import os
import time
import sys
import math

l1 = 0
l2 = 0
l3 = 0
R= ''

l1 = int (input('digite o tamanho: '))
l2 = int (input('digite o tamanho: '))
l3 = int (input('digite o tamanho: '))

if  l1 >= (l2+ l3) or l2 >= (l1+l3) or l3 >= (l2+l1):
     R=("Não é um triangulo")
else:     
    if l1 == l2 and l3 == l2:
        R=("triangulo equilátero!")
    elif l1!=l2 and l2!=l3 :
        R=("triangulo escaleno!")
    else: R = ("triangulo Isósceles!")
print(R)
time.sleep(5)
sys.exit( )