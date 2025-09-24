# -*- coding: utf-8 -*-
# Programa: somadigitos.py
# Programador:lk
# Data: 15/04/25
# Programa que le um número inteiro e calcula e imprime a soma dos dois 
# dígitos menos significativo do número lido (mais a direita).
# início do módulo principal
# descrição das variáveis utilizdas
# int intNum, umDigito, doisDigito, soma

# pré: intNum == d_k..d_1d_0 && 0 <= d_i <= 9

# Passo 1. Leia o numero inteiro
intNum = int(input())
# Passo 2. Calcule os dois digitos menos significativos
# Passo 2.1. Calcule o dígito menos significativo
umDigito = intNum%10
# Passo 2.2. Calcule o segundo dígito menos significativo

doisDigito = (intNum//10)%10
# Passo 3. calcule a soma dos dígitos
soma = umDigito + doisDigito
# Passo 4. Imprima os resultados
print('{0:d}'.format(soma))

# pós: soma == d_0 + d_1
# fim do módulo principal
