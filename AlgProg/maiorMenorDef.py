# -*- coding: utf-8 -*-
# Programa: maiorMenorDef.py
# Programador: Lorran Kaique
# Data: 08/07/2025
# Este programa retorna os maiores/menores e suas posicoes dada
#uma lista de numeros inteiros
#Como deve retornar o menor indice caso haja mais de um valor
#O ideal é percorrer do fim pro inicio
#Passo 0. Definir abstracoes
#Passo 0.1 Inicializar funcoes
def maiormenor(L):
    tam = len(L)
    maior = 0
    posMaior = 0
    for i in range((tam - 1), -1, -1):
        if maior <= L[i]:
            maior = L[i]
            posMaior = i
    menor = L[(tam-1)]
    posMenor = tam-1
    for i in range((tam - 2), -1, -1):
        if menor >= L[i]:
            menor = L[i]
            posMenor = i
    return maior, posMaior, menor, posMenor
#Passo 1. Ler a lista L
L = list(map(int, input().split()))
#Passo 2. Achar o maior menor e as posicoes
maior, posMaior, menor, posMenor = maiormenor(L)
#Passo 3. imprimir resultados
print(posMaior, maior, posMenor, menor)