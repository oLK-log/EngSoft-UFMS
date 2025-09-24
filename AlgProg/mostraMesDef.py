# -*- coding: utf-8 -*-
# Programa: mostraMes.py
# Programador: lorran kaique
# Data: 06/07/2025
# Este programa dado um numero imprime o mes correspondente
#Passo 0. Iniciar abstracoes
#Passo 0.1 variaveis

#Passo 0.2 iniciar funcoes
def mostrames(mes):
    mesesAno = ['Janeiro','Fevereiro','Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    if 1 <= mes <= 12:
        return mesesAno[mes - 1]
    else:
        return 'Número inválido'
#Passo 1. Ler entrada
entry = int(input())
#Passo 3.descobrir o mes:
resposta = mostrames(entry)
#Passo 4. Imprimir resposta
print(resposta)