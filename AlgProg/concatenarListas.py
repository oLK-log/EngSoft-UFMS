# -*- coding: utf-8 -*-
# Programa: concatenarListas.py
# Programador:Lorran Kaíque
# Data: 21/01/2013
# Este algoritmo, dada duas listas, deseja obter uma terceira que seja a junção intercalada
#das listas de entrada
#Entrada: list l1, l2
#saida: list l3
#Passo 0: inicalizar variaveis
#l3 = []
#Passo 1: ler as listas
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
#PAsso 2: definir tamanhos das listas
n1 = len(l1)
n2 = len(l2)
#Passo 3: concatenar as listas
l3 = [num for pair in zip(l1, l2) for num in pair]

#for i in range(len(l1)):
#    l3.append(l1[i])
#    l3.append(l2[i])
#l3 = sum(zip(l1, l2), ())
#Passo 4: Imprimir l3
print(l3)
#print(f"[{', '.join(map(str, l3))}]")