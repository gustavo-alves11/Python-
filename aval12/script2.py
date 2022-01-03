# -*- coding: utf-8 -*-
import os
import sys
import time

Sexo = ""
Salario = 0 
MediaM = 0
MediaF = 0
SaldoM = 0
SaldoF = 0
contM = 0 
contF = 0   

def lerSexo(): 
    global Sexo
    Sexo = str(input('Digite o sexo:'))
    if Sexo == "F" or Sexo == "f" or Sexo == "M" or Sexo == "m":
        return Sexo
    else: 
        print("Valor invalido digite F, f ou M, m")
        time.sleep(2)
def lerSalario(): 
    global Salario 
    Salario = int(input('Digite O salario:')) 
    return Salario


while True:
    os.system('cls') 
    tecla = str ( input ("\nmenu\n1 Ler dados\n2 Resultados\n3 Finalizar \nitem:") ) 
    if tecla == '1':
            lerSexo()
            
            if Sexo == "F" or Sexo == "f" or Sexo == "M" or Sexo == "m":
                lerSalario()
                if Sexo == "M" or Sexo == "m":
                    contM = contM+1   
                    SaldoM += Salario
                    MediaM = SaldoM/contM
                
                elif Sexo == "F" or Sexo == "f":
                    contF= contF+ 1   
                    SaldoF += Salario
                    MediaF = SaldoF/contF
            else: 
                print('Digite o sexo')
                time.sleep(3)
    elif tecla == '2':
        print('Informações dos salários dos homens')
        print('\nSaldo Acumulado=', SaldoM)
        print('\nMedia salarial=', MediaM)

        print('\n\nInformações dos salários das mulheres')
        print('\nSaldo Acumulado=', SaldoF)
        print('\nMedia salarial=', MediaF)
    
        time.sleep(10)
    elif tecla == '3':
        print('programa será finalizado')
        time.sleep(3)
        sys.exit()
    else: 
        print('Valor inválido!!!')
        time.sleep(3)
