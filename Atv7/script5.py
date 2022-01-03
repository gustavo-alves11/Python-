# -*- coding: utf-8 -*-
import os
import sys
import time

nome = 0
email = 0 
idade = 0 
telefone = 0
rua = 0 
numero = 0  
cep = 0 
bairro = 0 
cidade = 0 
estado = 0  
area = 0
pais = 0 
salario = 0 
tecla = 0
texto=0
def MenuProg():    
        tecla = int ( input ("\nmenu\n1 Executar\n2 Finalizar\nitem:") )
        os.system('cls') 
        
        if tecla == 1:
            nome = input ('Digite o nome:') 
            email = input ('Digite o email:') 
            idade = int(input ('Digite a idade:'))  
            telefone =int (input ('Digite o telefone:')) 
            rua = input ('Digite a rua:') 
            numero = int (input ('Digite o numero da casa:'))
            cep = int (input ('Digite o cep:') )
            bairro =  input ('Digite o bairro:') 
            cidade =  input ('Digite a cidade:') 
            estado =  input ('Digite o estado:') 
            area = input ('Digite a area de trabalho:') 
            pais = input ('Digite o pais:') 
            salario = int (input ('Digite o salario:'))
            texto = 'Hoje vou falar sobre %s, que tem %d anos nasceu em %s, %s onde mora até hoje na rua %s-%d no bairro %s (Cep: %d) .\nO %s adora seu pais (%s) devido a isso ele não pretende ir para outro pais. Inclusive está procurando um emprego\n na area de %s com salario em torno de %f e deixou aqui no escritorio formas de contato, seu email é %s \n e seu telefone é %d.' % (nome, idade, cidade, estado,rua, numero, bairro, cep, nome, pais, area, salario, email, telefone)
                                                                                                                    
            print(texto)
            time.sleep(20)      
            MenuProg()
            
        elif tecla == 2:
            time.sleep(20)      
            sys.exit()
MenuProg()