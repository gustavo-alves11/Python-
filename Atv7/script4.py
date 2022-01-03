# -*- coding: utf-8 -*-
import os
import sys
import time

A=0
Mr=0
R=0
tecla =0
def MenuProg():
    tecla = int ( input ("\nmenu\n1 Executar\n2 Finalizar\nitem:") )
    os.system('cls') 
    if tecla == 1:   
            A = int ( input ('Digite o valor de um número inteiro qualquer:') )
            Mr= A % 4
            if Mr == 0:
                R = ("Ano bissexto")
                print(R)
                time.sleep(5)     
                MenuProg()  
            if Mr != 0: 
                R = ("Ano não bissexto")       
                print(R)
                time.sleep(5)     
                MenuProg()        
    elif tecla == 2:      
        print("Fim do Programa!\n")      
        time.sleep(5)      
        sys.exit()
MenuProg()