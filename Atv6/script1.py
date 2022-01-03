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
os.system('clear');
tecla = int( input ("\nMenu\n1 Executar \n2 Sair\nItem:"))
if tecla == 1: 
    A = float (input('digite o numero: '))
    B = float (input('digite o numero: '))
    C = float (input('digite o numero: '))
    

    if A == 0:
        print("O valor de A não pode ser 0! ")
    elif A > 0:
        delta = (B ** 2) -4*A*C
        if delta >=0:
            X1 = (-B + delta ** (1 / 2)) / (2 * A)
            X2 = (-B - delta ** (1 / 2)) / (2 * A)
        elif delta <0: print ('Sem soluçao para esse valor de delta')
    print ( X1 )    
    print ( X2 )

    time.sleep(5)
    sys.exit()
elif tecla == 2:
    sys.exit() 