# -*- coding: utf-8 -*-
import os
import sys
import time

N1=0
N2=0
N3=0
N4=0
tecla =0
def MenuProg():
    
    tecla = int ( input ("\nmenu\n1 Executar\n2 Finalizar\nitem:") )
    os.system('cls') 
    if tecla == 1:   
            N1 = int ( input ('Digite o valor de um número inteiro qualquer:') )
            N2 = int ( input ('Digite o valor de um número inteiro qualquer:') )   
            N3 = int ( input ('Digite o valor de um número inteiro qualquer:') )
            N4 = int ( input ('Digite o valor de um número inteiro qualquer:') )
                 

            if N1 % 2 == 0 and N1 % 3 == 0:       
                print ( '\n', N1, ' é divisível por 2  e por 3')       
                print ( '\n Portanto, 2 e 3 são divisores de ', N1)   
        
            if N2 % 2 == 0 and N2 % 3 == 0:       
                print ( '\n', N2, ' é divisível por 2  e por 3')       
                print ( '\n Portanto, 2 e 3 são divisores de ', N2) 
            
            if N3 % 2 == 0 and N3 % 3 == 0:       
                print ( '\n', N3, ' é divisível por 2  e por 3')       
                print ( '\n Portanto, 2 e 3 são divisores de ', N3) 
            
            if N4 % 2 == 0 and N4 % 3 == 0:       
                print ( '\n', N4, ' é divisível por 2  e por 3')       
                print ( '\n Portanto, 2 e 3 são divisores de ', N4) 
                MenuProg()            
    elif tecla == 2:      
            print("Fim do Programa!\n")      
            time.sleep(5)      
            sys.exit()
MenuProg()