# -*- coding: utf-8 -*-
import os
import sys
import time

n=0
tecla =0
def MenuProg():
    tecla = int ( input ("\nmenu\n1 Executar\n2 Finalizar\nitem:") )
    if tecla == 1:   
        N = int ( input ('Digite o valor de um número inteiro qualquer:') )   
        os.system('clear') 

        if N % 2 == 0 and N % 3 == 0:       
            print ( '\n', N, ' é divisível por 2  e por 3')       
            print ( '\n Portanto, 2 e 3 são divisores de ', N)   
        else:       
            print('\n', N, ' NÃO é divisível por 2 e por 3!')   
            time.sleep(5)
        MenuProg()
    elif tecla == 2:      
        print("Fim do Programa!\n")      
        time.sleep(5)      
        sys.exit()

MenuProg()