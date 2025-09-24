# -*- coding: utf-8 -*-
# Programa: 
# Programador:Lorran Kaíque
# Data: 16/05/2025
# Este programa deve, a partir de uma lista de inteiros, encontrar o menor valor
#entradas: list lista
#saídas: int menor
#Passo 1: Ler lista
lista = list(map(int, input().split()))
#Passo 2: iterar para achar o menor valor
#Passo2.1. Inicializar variavel menor
menor = lista[0]
#Passo 2.2. Iterar
for i in lista:
    if menor > i:
        menor = i
#Imprimir valor
print(menor)