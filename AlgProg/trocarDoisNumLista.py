# -*- coding: utf-8 -*-
# Programa: MoverMenorNumero.py
# Programador:Lorran Kaique
# Data: 09/06/2016
# Este programa lê uma lista, computa a posicao do menor
#elemento da lista e troca o elemento com o da posicao 0
#Entradas: list int lista
#Saidas: int tam, pos
#Passo 0: Ler lista
lista = [int(s) for s in input().split()]
#PAsso 1: :Inicializar variaveis
tam = len(lista)
menor = lista[0]
#Passo 2: Achar o menor
for i in range(1, tam):
    if lista[i] < menor:
        menor = lista[i]
        pos = i
#Passo 3: Trocar as posicoes
lista[pos] = lista[0]
lista[0] = menor
#Passo 4: Imprimir
print(*lista)