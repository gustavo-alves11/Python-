import os
import sys 
import time

numero= 0
par=0
impar=0 
tecla=0

def defNumero():
    global numero
    numero= int(input('digite o numero: '))
    return numero

def CalcPar(numero):
    global par
    for i in range (1, numero+1):      
        if  i%2==0: 
            par = par+1
    return par

def CalcInpar(numero):
    global impar
    for i in range (1, numero+1):      
        if  i%2!=0: 
            impar = impar+1    
    return impar

def controle():    
    while True:
        os.system('cls') 
        tecla = str ( input ("\nmenu\n1 Ler dados\n2 Calcular \n3 Resultados\n4 Finalizar \nitem:") ) 
        if tecla == '1':
            defNumero()
        elif tecla == '2':
            CalcInpar(numero)
            CalcPar(numero)
        
        elif tecla == '3':
            print('\nNumero', numero)
            print('\ntotal de pares', par)
            print('\ntotal de impares', impar)
            time.sleep(10)
        
        elif tecla == '4':
            print('programa será finalizado')
            time.sleep(3)
            sys.exit()
        else: 
            print('Valor inválido!!!')
            time.sleep(3)
controle()