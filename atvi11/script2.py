# -*- coding: utf-8 -*-
import os
import sys
import time

def lerCapital(): 
    capital = float(input('Digite o capital inicial:')) 
    return capital

def lerJuros(): 
    juros = float(input('Digite o juros:')) 
    return juros

def lerperiodo(): 
    periodo = float(input('Digite o periodo:')) 
    return periodo

def calvalor(capital,juros,periodo): 
    valor = capital * juros * periodo 
    return valor

def exibir(capital,juros,periodo,valor): 
    os.system('cls') 
    print(f'Capital inicial:{capital}\nJuros:{juros}\nPeriodo:{periodo}\nValor do juros:{valor}\n')    
    time.sleep(7)

def controle(): 
    while True:   
        os.system('cls')   
        itenmenu=int(input('\n1 ler\n2 calcular\n3 exibir\n4 sair\nitem:'))   
        if itenmenu==1:      
            capital = 0      
            while capital==0:
                capital = lerCapital()
                juros = lerJuros()
                periodo = lerperiodo()               

        elif itenmenu == 2:  
            valor=calvalor(capital,juros,periodo)
        elif itenmenu==3:      
            exibir(capital,juros,periodo,valor)
        elif itenmenu==4:      
            print('O programa será finalizado!')      
            time.sleep(5)      
            sys.exit
        else:       
            print('Selecione um item válido!')       
            time.sleep(5)
controle()