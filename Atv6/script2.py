# -*- coding: utf-8 -*-
import os
import time
import sys

A = 0
B = 0
C = 0
T = True 

os.system('clear');
tecla = int( input ("\nMenu\n1 ler e exibir \n2 Sair\nItem:"))
   

if tecla == 1: 
    A = float (input('digite o numero: '))
    B = float (input('digite o numero: '))
    C = float (input('digite o numero: '))

    if A < B + C and B<A+C and C<A+B:
        T = True
    else: T = False
    if T == True:
        print('Trata-se de um triâgulo!')
    elif T == False:
        print ('Uma figura qualquer de tres lados')
    time.sleep(5)
    sys.exit()
elif tecla == 2:
    sys.exit() 