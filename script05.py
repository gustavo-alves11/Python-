# -*- coding: utf-8 -*-
import os
import time
import sys

A = 0
B = 0
C = 0
X1 = 0
X2 = 0
delta = 0 

A = float (input('digite o numero: '))
B = float (input('digite o numero: '))
C = float (input('digite o numero: '))
delta = (B ** 2) -4*A*C

if A == 0:
    print("O valor inválido")
else:
    X1 = (-B + delta ** (1 / 2)) / (2 * A)
    X2 = (-B - delta ** (1 / 2)) / (2 * A)


print ( X1 )
print ( X2 )

time.sleep(5)
sys.exit 