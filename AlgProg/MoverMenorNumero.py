# -*- coding: utf-8 -*-
# Programa: MoverMenorNumero.py
# Programador:Lorran Kaique
# Data: 09/06/2016
# Este programa lê uma lista, computa a posicao do menor
#elemento da lista e move esse elem para a 1ºposicao
#Entradas: list int lista
#Saídas: list int listaOrg
#Passo 1: Ler a lista
lista = list(map(int,input().split()))
#Passo 1.1:Iniciar variavel menor
#ele inicia com o lista[0]
menor = lista[0]
#Passo 2: Encontrar o menor elemento
for i in range(0, len(lista), 1):
    if menor > lista[i]:
        menor = lista[i]
        posicao = i
#Passo 3: Criar a nova lista substituindo
#Passo 3.1:Inicializar listaOrg
listaOrg = []
#Passo 3.2: Add valores
listaOrg.append(lista[posicao])
for x in range(0, len(lista), 1):
    if x != posicao:
        listaOrg.append(lista[x])
#Passo 4:IMprime
for i in range(0, len(listaOrg),1):
    print(listaOrg[i], end=" ")
print('\n')
###################################
#Utilizando funcoes
# Programa para ler um conjunto de itens, armazená-los numa lista,
# computar o menor elemento e mover para a primeira posição da lista,
# e então imprimir a lista modificada.
# início do módulo principal
# descrição das variáveis utilizadas
# list lista
# int menor, tam

# pré: lista[0]..lista[n-1]

# Passo 1. Leia um conjunto e armazene em uma lista
lista = [int(s) for s in input().split()]
# Passo 2. Mova o menor elemento para a primeira posição na lista
# Passo 2.1. Compute o menor elemento da lista
# Passo 2.1.1. Compute o tamanho da lista
tam = len(lista)
# Passo 2.1.2. Inicialize menor com o primeiro elemento da lista
menor = lista[0]
# Passo 2.1.3. Percorra os demais elementos da lista e compute menor
for i in range(1,tam):
   if lista[i] < menor:
      menor = lista[i]
# Passo 2.2. Retire menor da posição atual na lista
lista.remove(menor)
# Passo 2.3. Insira menor na primeira posição da lista
lista.insert(0,menor)
# Passo 3. Imprima a lista com menor na primeira posição
print(*lista)


        