# -*- coding: utf-8 -*-
# Programa: exer5
# Programador:Lorran Kaíque
# Data: 16/05/2025
# Este programa deve ler uma lista L, de tamanho tam
#ler o tam elementos da lista e por último o numero que indica
#o valor que queremos verificar se esta na lista
#entradas: int tam, list lista, int n
#saída: string res
#Passo 0: Inicializar variaveis
lista = []
res = 'não'
#Passo 1: Ler as entradas
#Passo 1.1. Ler o tam
tam = int(input())
#Passo 1.2. Com base no tam, fazer tam iterações que adicionam o valor a lista
for i in range(0, tam):
    lista.append(int(input()))
#Passo 1.3. Ler o n
n = int(input())
#Passo 2- Verificar se n contem na lista
for i in range(0, tam):
    if n == lista[i]:
        res = 'sim'
#Passo 4- Imprimir res
print(res)