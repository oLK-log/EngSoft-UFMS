# -*- coding: utf-8 -*-
# Programa: fibonaci02.py
# Programador: lORRAN kAÍQUE
# Data: 05/05/2025
# Este programa calcula o valor de e^x
#A entrada é dada por 2 números de onto flutuante
#entrada: float x, epsilon
#saída: float e
#variaiveis: soma, termo, n
#Passo 1: ler x e epsilon
x= float(input())
episilon= float(input())
#Passo 2: Definir variaveis
termo = 1.0
soma = termo
n = 1
div = 1
#Passo 3: Calcular
while termo >= episilon:
    termo *= x/n
    cima = x**n
    #print('o termo de cima é:', cima)
    baixo = n
    div = n
    while baixo >1:
        div *= (baixo-1)
        baixo-=1
    baixo = div
    #print('O termo de baixo é:', baixo)
    soma += cima / baixo
    #print('a soma é:', soma)
    n += 1
soma -= cima/baixo
print("{0:.7f}".format(soma))