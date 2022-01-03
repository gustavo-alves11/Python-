# -*- coding: utf-8 -*-# 
import os
import sys
import time
tecla = 0
while True:
    tecla = int ( input ("\nmenu\n1 Executar\n2 Finalizar\nitem:") )
    if tecla == 1:
        def lerComprimento():   
            comprimento = float ( input ('Comprimento:'))   
            return comprimento

        def calcDiametro(comprimento):   
            diametro= comprimento / 3.14
            return diametro

        def calcRaio(diametro):   
            raio = diametro/2   
            return raio

        def calcArea(raio):
            area= raio *raio * 3.14
            return area 

        def mostrar(diametro, raio, area):   
            os.system('cls')   
            print(f'\nDiametro = {diametro}')   
            print(f'\nRaio = {raio}')   
            print(f'\nArea = {area}')   
            time.sleep(5) 
                
        def executar():    
            comprimento = lerComprimento()    
            diametro = calcDiametro(comprimento)    
            raio = calcRaio(diametro)    
            area = calcArea(raio)
            mostrar(diametro, raio, area)
        executar()
        sys.exit
        MenuProg()
    elif tecla == 2:      
        print("Fim do Programa!\n")      
        time.sleep(5)      
        sys.exit()
MenuProg()