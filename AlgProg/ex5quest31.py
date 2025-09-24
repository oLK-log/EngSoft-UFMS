# -*- coding: utf-8 -*-
# Programa: exer5
# Programador:Lorran Kaíque
# Data: 16/05/2025
# Este programa le uma lista e o valor de um
#indice. Ele remove o elemento correspondente
#ao indice e imprime o valor e a nova lista
#entradas: list lista, int ind
#saidas: int valor, novaLista
#Passo 1.Ler lista e indice
lista = list(map(int, input().split()))
ind = int(input())
#Passo 2. Armazenar valos do ind
valor = lista[ind]
#Passo 3. Remover valor correspondente a posicao ind
lista.pop(ind)
#PAsso 4. Imprimir valor e lista
print(valor)
print('[{}]'.format(', '.join(map(str, lista))))