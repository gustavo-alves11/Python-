import os
import sys 
import time

Resultado = 0
numero= 0
tecla=0

def defNumero():
    global numero
    numero= int(input('digite o numero: '))
    return numero

def CalcFatoral(numero):
    global Resultado
    for i in range (0, numero+1):      
        if Resultado == 0:
            Resultado= i*(i)
        else: Resultado= i*Resultado
    return Resultado
def controle():      
    while True:
        os.system('cls') 
        tecla = str ( input ("\nmenu\n1 Ler dados\n2 Resultados\n3 Finalizar \nitem:") ) 
        if tecla == '1':
            defNumero()
            CalcFatoral(numero)
                
        elif tecla == '2':
            print('\nResultado=', Resultado)
            time.sleep(10)
        elif tecla == '3':
            print('programa será finalizado')
            time.sleep(3)
            sys.exit()
        else: 
            print('Valor inválido!!!')
            time.sleep(3)
controle()