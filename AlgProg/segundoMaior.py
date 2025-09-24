# -*- coding: utf-8 -*-
# Programa: segundoMaior.py
# Programador: lORRAN kAÍQUE
# Data: 05/05/2025
# Este programa le uma lista e informa o segundo maior número
#entrada: list lista
#variaveis: int n1
#saída: int n2
#Passo 1: Ler a lista
lista = list(map(int, input().split()))
#Passo 2: Inicializar variaveis
n1 = 0 #esse é o maior numero
n2 = 0 #esse é o segundo maior numero
contador = {}
repetidos = []
#Passo 3: percorrer a lista
#Passo 3.0- Encontrar os números repetidos da lista
for num in lista:
    if num in contador:
        if num not in repetidos: #se n estiver em repetido
            repetidos.append(num)
    else:
        contador[num] = 1
#Passo 3.1-Encontrar o maior valor
for num in lista:
    if num > n1:
        n1 = num
#PAsso 3.2-Encontrar o segundo maior
for num in lista:
    if num > n2 and num < n1:
        n2 = num
#Passo 3.3-Se forem iguai, n2 = n1
for reper in repetidos:
    if reper == n1:
        n2 = n1
#Passo 4: Imprimir
print(n2)