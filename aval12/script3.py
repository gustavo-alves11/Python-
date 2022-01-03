# -*- coding: utf-8 -*-
import os
import sys
import time

Idade = 0
Pagamento = 0 
MaiorpagamentoAdultos = 0
MenorpagamentoAdultos = 0
Maiorpagamento = 0
Menorpagamento = 0
contmaiores = 0
cont=0 
   

def leridade(): 
    global Idade
    Idade = int(input('Digite a idade:'))
    return Idade

def lerPagamento(): 
    global Pagamento
    Pagamento = int(input('Digite O pagamento:')) 
    return Pagamento


while True:
    os.system('cls') 
    tecla = str ( input ("\nmenu\n1 Ler dados\n2 Resultados\n3 Finalizar \nitem:") ) 
    if tecla == '1':
            leridade()
            
            if Idade >= 18:
                lerPagamento()
                while contmaiores == 0:
                    MaiorpagamentoAdultos = Pagamento
                    MenorpagamentoAdultos = Pagamento
                    contmaiores = contmaiores+1
                
                if MaiorpagamentoAdultos < Pagamento:
                    MaiorpagamentoAdultos = Pagamento
                elif MenorpagamentoAdultos > Pagamento:
                    MenorpagamentoAdultos = Pagamento
                contmaiores = contmaiores+1

            elif Idade < 18:
                lerPagamento()
                while cont == 0:
                    cont = cont+1
                    Maiorpagamento = Pagamento
                    Menorpagamento = Pagamento
                
                if Maiorpagamento < Pagamento:
                    Maiorpagamento = Pagamento
                elif MenorpagamentoAdultos > Pagamento:
                    Maiorpagamento = Pagamento
                cont = cont+1
    elif tecla == '2':
        print('Pagamentos maiores de 18')
        print('\nMaior pagamento=', MaiorpagamentoAdultos)
        print('\nMenor pagamento=', MenorpagamentoAdultos)
        print('\nQuantidade de maiores de 18=', contmaiores)

        print('\n\nPagamentos menores de 18')
        print('\nMaior pagamento=', Maiorpagamento)
        print('\nMenor pagamento=', Menorpagamento)
        print('\nQuantidade de menores de 18=', cont)
    
        time.sleep(10)
    elif tecla == '3':
        print('programa será finalizado')
        time.sleep(3)
        sys.exit()
    else: 
        print('Valor inválido!!!')
        time.sleep(3)
