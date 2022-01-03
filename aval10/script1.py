# -*- coding: utf-8 -*-# 
import os
import sys
import time
tecla =0
def MenuProg():
    tecla = int ( input ("\nmenu\n1 Executar\n2 Finalizar\nitem:") )
    if tecla == 1:
        def lerN1():   
            n1 = float ( input ('Nota1:'))   
            return n1

        def lerN2():   
            n2 = float ( input ('Nota2:'))   
            return n2

        def getMedia(n1, n2):   
            media = (n1+n2)/2   
            return media

        def mostrar(media):   
            os.system('cls')   
            print(f'\nMédia = {media}')   
            if media < 6:      
                print('\nAluno Reprovado')  
            else:      
                print('\nAluno Aprovado')    
            time.sleep(5) 
                
        def executar():    
            nota1 = lerN1()    
            nota2 = lerN2()    
            media = getMedia(nota1, nota2)    
            mostrar ( media )
        executar()
        sys.exit
        MenuProg()
    elif tecla == 2:      
        print("Fim do Programa!\n")      
        time.sleep(5)      
        sys.exit()
MenuProg()