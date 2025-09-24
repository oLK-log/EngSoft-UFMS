# -*- coding: utf-8 -*-
# Programa: mediaalturas00.py
# Programador:Lorran Kaique
# Data: 15/05/2025
# Este programa lê um conjunto de alturas, conta-as calcula e
# imprime a média, e o número de alturas maiores ou iguais a média.
# A entrada é dada por uma lista de n números reais (alturas), uma
# em cada linha, e a ultima linha contém o número 0.0 que sinaliza
# o final da entrada. Use o append() para ler os elementos da lista.
# A saída consiste em imprimir a média e a quantidade de alturas
# que são maiores ou iguais a média. O valor da média das alturas
# deve ser impresso com duas casas decimais ({0:.2f}).
# início do módulo principal
# descrição das variáveis utilizadas
# list  alturas[]
# float media
# int   num, tam
#Passo 0: Definir variáveis
a : float #entrada do valor
a = 1
lista : list #lista criada
lista = []
tam : int
media : float #media das alturas
media = 0.0
altMaiorIgual : int #qtd altura maior ou igual a média
altMaiorIgual = 0
# pré: alturas[0]..alturas[tam-1]
#Passo 1: Ler as alturas e armazenar em uma lista
while a != 0.0:
    a = float(input())
    if a != 0.0:
        lista.append(a)
#Passo 2: Calcular a média
#Passo 2.1- Calcular o tamanho da lista
tam = len(lista)
for i in range(0,tam):
    media += lista[i]
media = media / (tam)
#Passo 3: Calcula qtd de valores que são >= media
for i in range(0,tam):
    if lista[i] >= media:
        altMaiorIgual += 1
#Passo 4: Imprimir valores
print('{0:.2f}\n{1:d}'.format(media, altMaiorIgual))
# pós: media and num
# fim do módulo principal
