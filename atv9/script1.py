# -*- coding: utf-8 -*-
import os
import sys
import time

Valor=0
Txjuros= 1/100
Dias=0
Multa=0
TxMulta= 2/100 
Vlpagar = 0
Juros = 0
tecla =0

while True:
    os.system('cls') 
    tecla = int ( input ("\nmenu\n1 Executar\n2 Resultados\n3 Finalizar \nitem:") )
    if tecla == 1:
            Valor = int ( input ('Valor') )
            Dias = int ( input ('Dias') )
            if Dias > 0:   
                Multa = TxMulta * Valor
                Juros = Txjuros * 1/30 * Dias * Valor
                Vlpagar = Valor + Multa + Juros           
    elif tecla == 2:      
        print('A multa é: ',Multa)
        print('O valor a pagar é: ', Vlpagar)
        print('A multa é: ',Juros)
        print('O valor é: ', Valor)
        print('O total de dias é: ',Dias)
        time.sleep(15)
    elif tecla == 3:      
        print('Finalizado')
        time.sleep(3)
        sys.exit
    else: 
        print('Selecione um item valido')
        time.sleep(3)
        

    
