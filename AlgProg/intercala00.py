# -*- coding: utf-8 -*-
# Programa: intercala00.py
# Programador: LORRAN
# Data: 21/05/25
# Este programa lê dois lista a e b de inteiros, do mesmo
# tamanho, computa a intercalação de a e b e imprime o
# resultado 
# Intercalação de listas de mesmo tamanho.
# a == [1, 3, 5, 7, 9]
# b == [4, 2, 8, 6, 10]
# a intercalado com b
# c = [a[0],b[0],a[1],b[1],a[2],b[2],a[3],b[3],a[4],b[4]]
# nesse caso específico, as duas tem o mesmo tamanho
# c = [1,4,3,2,5,8,7,6,9,10]
# início do módulo principal
# descrição das variáveis utilizadas
# list a, b, c
# int tam

# pré: a[0]..a[tam-1] b[0]..b[tam-1]
#Passo 0: inicializar variaveis
va = 0
vb = 0
# Passo 1. Leia as listas
# Passo 1.1. Leia o vetor a
a = list(map(int, input().split()))
# Passo 1.2. Leia o vetor b
b = list(map(int, input().split()))
# Passo 1.3. Calcule o tamanho das listas
n1 = len(a)
n2 = len(b)
# Passo 2. Intercale as listas
c = []
n3 = n1 + n2
for i in range(0, n3):
    if i % 2 == 0:
        c.append(a[va])
        va += 1
    else:
        c.append(b[vb])
        vb+=1
# Passo 3. Imprima as listas intercaladas
print(c)

# pós: c == [a[0], b[0],..,a[tam-1], b[tam-1]
# fim do módulo principal
