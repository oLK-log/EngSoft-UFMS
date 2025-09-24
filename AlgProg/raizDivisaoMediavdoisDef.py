# -*- coding: utf-8 -*-
# Programa: raizDivisaoMediaDef.py
# Programador: Lorran Kaique
# Data: 06/07/2025
# Este programa deseja computar a raiz quadrada aproximada de
#um dado numero por meio de uma funcao raizq
#pensamento: 3 parametro: numero, aprox, epsilon
#formula simplif: newAprox = (aprox + num / aprox) / 2.0
#só para qunado a diferenca aprox - newAprox < epsilon
#Passo 0. definir abstracoes
#Passo 0.1 criar funcoes
def raizq(num, aprox, epsilon):
    while True:
        if abs(aprox-(num/aprox)) < epsilon:
            break
        aprox = (aprox + num / aprox) / 2.0
    return aprox
#Passo 1. Ler entradas
num = float(input())
epsilon = float(input())
aprox = float(input())
#Passo 2. Encontrar raiz
resultado = raizq(num,aprox,epsilon)
#Passo 3. Imprimir
print(f'{resultado:.6f}')