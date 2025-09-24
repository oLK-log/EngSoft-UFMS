# -*- coding: utf-8 -*-
# Programa: semrepeticao.py
# Programador:lorran kaique
# Data: 21/05/25
# Este programa lê uma lista de  n itens, retira os elementos
# repetidos da lista e imprime o resultado.
#entradas: list lista
#saida: list semRep
#Passo 0:inicializar variaveis
n = 1
#Passo 1: Ler entradas
lista = list(map(int, input().split()))
tam = len(lista)
repetidos = []
#Passo 2:iterar para encontrar el repetidos
for elemento in lista:   
    for i in range(n, tam):
        if elemento == lista[i]:
            repetidos.append(i)
    n += 1
#Passo 3: Remover esses repetidos da lista
    for rep in reversed(repetidos):
        del lista[rep]
    repetidos = []
    tam = len(lista)
#Imprimir lista sem repetições
print(f"[{', '.join(map(str, lista))}]")