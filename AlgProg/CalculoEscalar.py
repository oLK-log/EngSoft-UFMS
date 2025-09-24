# -*- coding: utf-8 -*-
#Programa: CalculoEscalar
#Programador: Lorran Kaíque
#Data: 09/05/2025
#Este programa le um arranjo de floats a de tamanho tam e o escalar l
#computa e imprimi a multiplicacao escalar b = l*a
#entradas: list a, int l
#saida: float b
#variaveis: int tam
#Passo 1: Ler lista e l
a = list(map(float, input().split()))
#a = [int(num) for num in input().split()]
l = float(input())
#Passo 2: Calcular nova lista b
tam = len(a)
b = []
for i in range(0, tam):
    b.append(l*a[i])
#Imprimir lista b
print('[ {0:f} ]'.format(*b), sep="")