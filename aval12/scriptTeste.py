# -*- coding: utf-8 -*-
import os
import sys

soma=0
def somapar (inicio, fim):   
    global soma   
    while  inicio <= fim:     
        if   inicio % 2 == 0:          
            soma += inicio     
        inicio+=1   
    print ('A soma dos pares é:', soma)
# Executando a Soma a Sub rotina
somapar ( 10,  20 ) # chamada por valor
x = 5
y = 10
somapar ( x, y ) # chamada por referenciasys.exit