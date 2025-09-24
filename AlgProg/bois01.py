# -*- coding: utf-8 -*-
# Programa: bois01.py
# Programador:
# Data: 27/10/2020
# Este programa lê um conjunto de dados referentes ao número de
# identificação e o peso dos bois em um frigorífico. O número de
# identificação igual a zero é usado com flag para sinalizar o
# final da entrada. O programa calcula a média dos pesos e o
# peso do boi mais gordo e o peso do boi mais magro, e quantos
# bois obtiveram esses pesos.
# início do módulo principal
# descrição das variáveis utilizadas
# list numeros, pesos
# int   numero     - número de identificação do boi
#       numbois    - número de bois
#       gordo      - número do boi mais gordo
#       magro      - número do boi mais magro
# float peso       - peso do boi
#       maiorPeso  - peso do maior boi
#       menorPeso  - peso do menor boi
#       soma       - soma dos pesos dos bois
#       media      - media dos pesos  

# pré: numeros[0] pesos[0]...numeros[numbois-1]
#      pesos[numbois-1]

# Passo 1. Inicialize as variáveis e leia a entrada
# Passo 1.1. Inicialize as variáveis
maiorpeso = 0.0
menorpeso = 5000.0
soma = 0.0
numbois = 0
numgordo = 0
nummagro = 0
numeros = []
pesos = []
# Passo 1.2. Leia o número e o peso do primeiro boi
numero =int(input())
# Passo 1.3. Enquanto numero > 0 faça
while numero > 0:
    numeros.append(numero)
    peso = float(input())
    pesos.append(peso)
    numbois += 1
    numero = int(input())
# Passo 2. Calcule a média
for i in range(0, numbois):
    soma+= pesos[i]
media = soma/numbois
#Passo 3. Maior peso e quantos bois tiveram esse peso
for i in range(0, numbois):
    if maiorpeso < pesos[i]:
        maiorpeso = pesos[i]
for i in range(0, numbois):
    if maiorpeso == pesos[i]:
        numgordo += 1
#Passo 4. Menor peso e quantos bois tiveram esse peso
for i in range(0, numbois):
    if menorpeso > pesos[i]:
        menorpeso = pesos[i]
for i in range(0, numbois):
    if menorpeso == pesos[i]:
        nummagro += 1
# Passo 4. Imprima os resultados
# Passo 4.1. Imprima a média dos pesos dos bois
print('{0:.2f}'.format(media))
# Passo 4.2. Imprima o número de bois mais gordo e seu peso
print('{0:.2f} {1:.0f}'.format(maiorpeso, numgordo))
# Passo 4.3. Imprima o número de bois mais gordo e seu peso
print('{0:.2f} {1:.0f}'.format(menorpeso, nummagro))

# pós: soma == Soma i em {0..n-1}:peso[i] and media ==
#      soma/numbois and maiorPeso == max{peso[0]..peso[i-1]} and
#      numgordo == Num i em {0..n-1}:peso[i] == maiorPeso and
#      menorPeso == min{peso[0]..peso[i-1]} and
#      nummagro == Num i em {0..n-1}:peso[i] == menorPeso
# fim do módulo principal
