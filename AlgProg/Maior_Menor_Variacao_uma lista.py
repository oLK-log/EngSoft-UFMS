# -*- coding: utf-8 -*-
# Programa: fibonaci02.py
# Programador: lORRAN kAÍQUE
# Data: 05/05/2025
# Este programa retorna o maior e o menor em uma lista de inteiros
#Passo 1: Ler a lista
lista = list(map(int, input().split()))
#Passo 2: Encontrar os indices max e min
#Passo 2.1-Inicializar as variaveis
indMax = 0
indMin = 0
#Passo 2.2- Percorrer a lista
for i in range(len(lista)):
    if lista[i] > lista[indMax]:
        indMax = i
    if lista[i] < lista[indMin]:
        indMin = i
#Passo 3- Encontrar o valor Max e min e variação
#Passo 3.1- valor MAx e Min
valorMax = lista[indMax]
valorMin = lista[indMin]
#Passo 3.2- variação
variacao = valorMax - valorMin
#Passo 4- Imprimir
print(indMax, valorMax, indMin, valorMin, variacao)
