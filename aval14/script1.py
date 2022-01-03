import os
import sys 
import time

N= 0
cont=0 
total = 0
tecla=0


def defNumero():
    global N
    N= int(input('digite o numero: '))
    return N

def primos(N):
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

def parImpar(N):
    cont = 0;
    if N % 2 == 0:
        cont = 1;
    
    if cont ==1:
        return True
    else:
        return False
    
def controle():    
    while True:
        os.system('cls') 
        tecla = int ( input ("\nmenu\n1 Ler dados\n2 Calcular \n3 Resultados\n4 Finalizar \nitem:") ) 
        if tecla == 1:
            defNumero()
        elif tecla == 2:
            primos(N);
            somarPrimos(N);
            parImpar(N);
        elif tecla == 3:
            if parImpar(N) == True :
                print('\nO numero é par')
            else: 
                print('\n O numero é impar')
                
            if primos(N): 
                print('\nO numero', N, 'é primo')
                print('\n A soma dos numeros primos é:',total)
            else: print('\nO numero não é primo')
            time.sleep(10)
        
        elif tecla == 4:
            print('programa será finalizado')
            time.sleep(3)
            sys.exit()
        else: 
            print('Valor inválido!!!')
            time.sleep(3)
controle()