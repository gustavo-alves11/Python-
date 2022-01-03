# -*- coding: utf-8 -*-
import os
import sys
import time
import math

def lerA(): 
    a = float(input('Digite A:')) 
    return a

def lerB(): 
    b = float(input('Digite B:')) 
    return b

def lerC(): 
    c = float(input('Digite C:')) 
    return c

def calDelta(a,b,c): 
    delta = math.pow( b , 2 ) - 4 * a * c 
    return delta

def anaStatus ( delta ): 
    if delta<0:   
        return "Impossível Calcular! Delta é negativo!" 
    elif delta == 0:   
        return "Duas raizes reais iguais!" 
    else:   return "Duas raizes reais diferentes!"

def calX1(a,b,delta): 
    x1 = (-b + math.sqrt(delta))/(2*a) 
    return x1

def calX2(a,b,delta): 
    x2 = (-b - math.sqrt(delta))/(2*a) 
    return x2

def exibir(a,b,c,delta,status): 
    os.system('cls') 
    print(f'Valor a:{a}\nValor B:{b}\nValorC:{c}\nDelta:{delta}\nStatus:{status}') 
    if delta >=0:   
        x1 = calX1(a,b,delta)   
        x2 = calX2(a,b,delta)   
    print(f'Valor x1:{x1}\nValor x2:{x2}')   
    time.sleep(7)
def controle(): 
    while True:   
        os.system('cls')   
        itenmenu=int(input('\n1 ler\n2 calcular\n3 exibir\n4sair\nitem:'))   
        if itenmenu==1:      
            a = 0      
            while a==0:
                a = lerA()      
                b = lerB()     
                c = lerC()
        elif itenmenu == 2:      
            delta = calDelta(a,b,c)      
            status = anaStatus( delta )
        elif itenmenu==3:      
            exibir(a,b,c,delta,status)
        elif itenmenu==4:      
            print('O programa será finalizado!')      
            time.sleep(5)      
            sys.exit
        else:       
            print('Selecione um item válido!')       
            time.sleep(5)
controle()