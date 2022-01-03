# -*- coding: utf-8 -*-
import os
import sys
import time

Nome = ''
Salario = 0 
MaiorSalario = 0
MenorSalario = 0
Media =0
Saldo = 0
global cont
cont = 0   
def lerNome(): 
    Nome = str(input('Digite o nome:')) 
    return Nome
def lerSalario(): 
    global Salario 
    Salario = int(input('Digite O salario:')) 
    return Salario

def Media(Saldo, cont):
    global Media
    Media = Saldo/cont
    return Media

while True:

    os.system('cls') 
    tecla = int ( input ("\nmenu\n1 Ler dados\n2 Resultados\n3 Finalizar \nitem:") ) 
    if tecla == 1:
        lerSalario()
        while cont == 0:
            lerNome()
            MenorSalario = Salario
            MaiorSalario = Salario
            cont= cont+1   
            Saldo = Salario
            Media = Saldo/cont
        
        if Salario >= MaiorSalario:
            MaiorSalario = Salario
        else: MaiorSalario = MaiorSalario
        if Salario <= MenorSalario:
            MenorSalario = Salario
        else: MenorSalario = MenorSalario
        cont= cont+ 1   
        Saldo += Salario
        Media = Saldo/cont

    elif tecla == 2:
        print('Nome=', Nome)
        print('\nSaldo Acumulado=', Saldo)
        print('\nMaior salario=', MaiorSalario)
        print('\nMenor Salario=', MenorSalario)
        print('\nMedia salarial=', Media)
        
        time.sleep(10)
    elif tecla == 3:
        print('programa será finalizado')
        time.sleep(2)
        sys.exit()
