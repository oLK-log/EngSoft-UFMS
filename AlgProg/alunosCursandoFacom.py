# -*- coding: utf-8 -*-
# Programa: alunosCursandoFacom.py
# Programador:Lorran Kaíque
# Data: 21/01/2013
# Este algoritmo tem como fim a intersecção de alunos cursando AlgProg1(API) e IntroSistemas(ISD)
#a entrada é dada por um numero inteiro-tamanho lista- e a lista, para cada matéria
#a saída consiste numa lista com os rga's da instersecção
#entrada: int n1, n2; list l1, l2
#saída: list l3
#Passo 0: Iniciar as variáveis
l3 =[]
#PAsso 1: Ler as entradas
n1 = int(input())
l1 = list(map(int, input().split()))
n2 = int(input())
l2 = list(map(int, input().split()))
#Passo 2: Comparar cada elemento de uma lista com os elementos da outra
for i in range(0,n1):
    for x in range(0, n2):
        if l1[i] == l2[x]:
            l3.append(l1[i])
#Passo 3: Imprimir a l3
print(f"[{', '.join(map(str, l3))}]")