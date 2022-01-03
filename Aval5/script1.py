# -*- coding: utf-8 -*-
import os
import time
import sys
import math 

NumLados = 0
MedLado = 0 
P = 0
A= 0 
Area = 0

NumLados = float(input('digite o numero de lados: '))
MedLado = float(input('Digite o tamanho dos lados: '))


if NumLados == 3:  
    P = ((MedLado+ MedLado+ MedLado)/2)
    Area = math.sqrt(P)*(3*(P-MedLado)) 
    print(f'Um triangulo de area: {Area:.2f}')

elif NumLados == 4: 
    Area= MedLado*MedLado
    msg= (f'Quadrado de area: {Area:.2f}')
    
elif NumLados == 5:
    
    P=5*MedLado/2 
    A=(MedLado/2)/math.tan(36)
    Area = P*A
   
    msg = (f'Poligono de area: {Area:.2f}')

else: print("Quantidade de lados invalida")
print(msg)

time.sleep(5)
sys.exit()