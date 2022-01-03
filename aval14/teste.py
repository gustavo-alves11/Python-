import os
import sys 
import time

N=0;
total=0;
N1 =0;

N= int(input('digite o numero: '))
def primos(N):
    global cont;
    cont=0;
    for i in range (N):  #esse for serve para analizar o numero digitado     
        if N % (i+1) == 0: 
            cont +=1;
    if cont == 2:
        return True
    else: 
        return False


def somarPrimos(N):
    global total;
    for X in range (0, N+1): # coloquei N+1 por que o ultimo numero nao ia para a função primos()
        primos(X);
       
        if primos(X):
          total= total+X
    return total

somarPrimos(N);
print(total)
########## POSSIVEL SOLUÇÃO!!!!!!!!!!
# criar 2 funçoes um igual o que está acima e outra ultilizará essa para somar os numeros primos.