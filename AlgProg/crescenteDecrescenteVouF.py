# -*- coding: utf-8 -*-
# Programa: crescenteDecrescenteVouF.py
# Programador: lORRAN kAÍQUE
# Data: 05/05/2025
# Este programa lê uma lista, verifica se estão em ordem crescente
# e retorna verdadeiro ou falso
#entradas: list lista
#saida: str res
#variaveis:
#boolean: decrescente
#Passo 1: Ler a lista
lista = list(map(int, input().split()))
#Passo 2: Inicializar variaveis
decrescente = True
#Passo 3: Percorrer a lista
#aqui vamos verificar se cada elemento é maior que o próximo
for i in range(len(lista) - 1):
    if lista[i] <= lista[i + 1]:
        decrescente = False
        break
#Passo 4: Imprimir
print('verdadeiro' if decrescente else 'falso')
             