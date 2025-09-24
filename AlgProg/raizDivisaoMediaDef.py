# -*- coding: utf-8 -*-
# Programa: raizDivisaoMediaDef.py
# Programador: Lorran Kaique
# Data: 06/07/2025
# Este programa deseja computar a raiz quadrada aproximada de
#um dado numero por meio de uma funcao raizq
#pensamento: 3 parametro: numero, aprox, epsilon
#formula simplif: newAprox = (aprox + num / aprox) / 2.0
#só para qunado a diferenca aprox - newAprox < epsilon
#a = numero -sempre o mesmo
#x = aproximacao
#Passo 0. definir abstracoes
#Passo 0.1 criar funcoes
def raizq(a, epsilon, x):
    a_x= a / x
    while True:
        if abs(x - (a/x)) < epsilon:
            break
        x = (x + (a/x)) / 2.0
    return x
#Passo 1. Ler entradas
a = float(input())
epsilon = float(input())
aprox = float(input())
#Passo 2. Encontrar raiz
resultado = raizq(a, epsilon, aprox)
#Passo 3. Imprimir
print(f'{resultado:.6f}')