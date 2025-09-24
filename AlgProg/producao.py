# -*- coding: utf-8 -*-
# Programa: producao.py
# Programador: Lorran Kaíque
# Data: 05/05/2025
# Este programa le a produção semanal de álcool de uma dada usina e
# calcula e imprime a soma da produção da semana.

# início
#Passo 0. Iniciar variaveis
soma = 0
# Passo 1. Leia e armazene a lista dos dados
lista = list(map(float,input().split()))
# Passo 2. Calcule a soma do vetor
for i in range(0, (len(lista)), 1):
    soma += lista[i]
# Passo 3. Imprima a produção da semana
print('{0:.2f}'.format(soma))

# fim