# -*- coding: utf-8 -*-
# Programa: seno.py
# Programador: lORRAN kAÍQUE
# Data: 05/05/2025
# Este programa define se um dado num é deficiente, perfeito ou abundadente
#deficiente: soma dos divisores próprios < num
#perfeito: soma divisores = num
#abundante: soma > num
#entrada: intervalo de números
#saída: o que cada número nesse intervalo é
#Passo 1: ler intervalo de números
n1, n2 = map(int,input().split())
#Passo 1.2: iniciar variaveis
soma = 0
#Passo 2: percorrer o intervalo
for i in range(n1, (n2+1), 1):
    for r in range(1,i,1):
        if i % r == 0:
            soma += r
#Passo 3: Lógica e impressão
    if soma > i:
        print(i,' abundante')
    elif soma == i:
        print(i,' perfeito')
    else:
        print(i,' deficiente')
    soma = 0