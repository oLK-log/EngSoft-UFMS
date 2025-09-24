# -*- coding: utf-8 -*-
# Programa: MoverMenorNumero.py
# Programador:Lorran Kaique
# Data: 06/05/2025
#O programa le um conjunto de dados referente
#ao numero de ident e o peso dos bois e armazena-os
#numa lista
#entradas: int n. list numero, peso
#saida: float media, qtd
#Passo 1: ler entradas
#PAsso 1.1 Ler número de bois
n = int(input())
#Passo 1.2 Ler numero e peso dos bois
#Passo 1.2.1 Iniciar lista
numero = [0]*n
peso = [0.0]*n
#Passo 1.2.2 Ler
for i in range(0, n):
    numero[i] = int(input())
    peso[i] = float(input())
#Passo 1.3 Inicializar variaveis
media = 0.00
acimaM = 0
#Passo 3: CAlcular a média
for i in range(0, n):
    media += peso[i]
media = media / n
#Passo 4: Encontrar valores acima da média
for i in range(0, n):
    if peso[i] > media:
        acimaM += 1
#Passo 4.1: Outra forma mais direta de implementar
        acimaM = sum([pesos > media for pesos in peso])
#Passo 5: Imprimir saidas
print('Média dos pesos de {0:d} bois = {1:.2f} Kg\nNúmero de bois com peso acima da média = {2:d}'
.format(n, media, acimaM))