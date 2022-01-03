# -*- coding: utf-8 -*-
import os
import sys
import time

N1=0
N2=0
N3=0
N4=0
N5=0
R=0
tecla =0
def MenuProg():
    tecla = int ( input ("\nmenu\n1 Executar\n2 Finalizar\nitem:") )
    os.system('cls') 
    if tecla == 1:   
            N1 = int ( input ('Digite o valor de um número inteiro qualquer:') )
            N2 = int ( input ('Digite o valor de um número inteiro qualquer:') )   
            N3 = int ( input ('Digite o valor de um número inteiro qualquer:') )
            N4 = int ( input ('Digite o valor de um número inteiro qualquer:') )
            N5 = int ( input ('Digite o valor de um número inteiro qualquer:') )
            R= max(N1,N2,N3,N4,N5)  
            print('o maior numero é',R)      
            time.sleep(5)     
            MenuProg()        
    elif tecla == 2:      
        print("Fim do Programa!\n")      
        time.sleep(5)      
        sys.exit()
MenuProg()