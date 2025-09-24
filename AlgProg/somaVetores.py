# -*- coding: utf-8 -*-
# Programa: somavetores.py
# Programador:Lorran Kaique
# Data: 15/05/2025
# Este programa le dois vetores de inteiros e computa imprime a soma
# início do módulo principal
# descrição das variáveis utilizadas
# list a, b, soma
# int tam

# pré: a b
#Cada vetor é uma lista, e o intuito é realizar a soma dos elementos da lista
#Declarar
a : list
b : list
soma : list
soma = []
# Passo 1. Leia os vetores
# Passo 1.1. Leia o vetor a
a = list(map(float, input().split()))
# Passo 1.2. Leia o vetor b
b = list(map(float, input().split()))
#Passo 1.3. Calcular o tamanho das lista
tamA = len(a)
tamB = len(b)
#Passo 1.4. Encontrar a maior lista e guardar a informacao
if tamA < tamB:
    menor = tamA
    maior = tamB
    Lmaior = b
else:
    maior = tamA
    menor = tamB
    Lmaior = a
# Passo 2. Calcule a soma dos vetores
for i in range(0, menor):
    soma.append(a[i]+b[i])
for x in range(menor,  maior):
    soma.append(Lmaior[x])
# Passo 3. Imprima o vetor soma
print(*soma)

# pós: soma and para i em {0..tam-1}:soma[i] == a[i]+b[i]
# fim do módulo principal
