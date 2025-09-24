# -*- coding: utf-8 -*-
# Programa: seno.py
# Programador: lORRAN kAÍQUE
# Data: 05/05/2025
# Este programa calcula o valor de sen(x)
#A entrada é dada por 2 números de ponto flutuante
#entrada: float x, epsilon
#saída: float senx
#variaiveis: termo, soma, n
#Passo1: Ler
x = float(input())
episilon = float(input())
#Passo 2: criar variaveis
termo = x
soma = termo
n = 3
v = False
#Passo 3:somar os termos
while termo >= episilon:
    termo *= -x**2 / ((2*n) * (2*n+1))
    cima = x**n
    baixo = n
    div = n
    while baixo >1:
        div *= (baixo-1)
        baixo-=1
    baixo = div
    n += 2
    if v == True:
        soma += cima / baixo
        v = False
    else:
        soma -= cima/baixo
        v = True
    n += 1
if v == True:
        soma -= cima / baixo
        v = False
else:
    soma += cima/baixo
    v = True
print('sen({0:+8.6f}) = {1:+8.6f}'.format(x, soma))
