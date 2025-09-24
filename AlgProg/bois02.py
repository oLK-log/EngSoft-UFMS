# -*- coding: utf-8 -*-
# Programa: bois02.py
# Programador: lorran kaique
# Data: 21/05/25
# Este programa lê um conjunto de dados referentes ao número de
# identificação e o peso dos bois em um frigorífico. O número de
# identificação igual a zero é usado com flag para sinalizar o final
# da entrada. O programa calcula a média dos pesos e o peso do boi
# mais gordo e o peso do boi mais magro.
# iníciio do módulo principal
# descrição das variáveis utilizadas
# descrição das variáveis utilizadas
# list  numeros, pesos
# int   numbois    - número de bois
#       numero     - número do boi
#	    gordo1     - número do boi mais gordo
#       gordo2     - número do segundo boi mais gordo
#       magro1     - número do boi mais magro
#       magro2     - número do segundo boi mais magro
# float peso       - peso do boi
#       maiorPeso1 - peso do boi mais gordo
#       maiorpeso2 - peso do segundo boi mais gordo
#       menorPeso1 - peso do boi mais magro
#       menorpeso2 - peso do segundo boi mais magro
#       soma       - soma dos pesos dos bois
#       media      - media dos pesos  

# pré: numeros[0] pesos[0] numeros[1] numeros[2] ..
#      numeros[numbois-1] pesos[numbois-1]

# Passo 1. Leia o número do primeiro boi e inicialize as variáveis
# Passo 1.1. Leia o número e o peso do primeiro boi
# print('Leia o número do boi - 0 para finalizar: ', end='')
numero = float(input())
# Passo 1.2. Inicialize as variáveis
maiorpeso = 0.0
maiorpeso2 = 0.0
menorpeso = 5000.0
menorpeso2 = 5000.0
soma = 0.0
numbois = 0.0
gordo1 = 0.0
gordo2 = 0.0
magro1 = 0.0
magro2 = 0.0
numeros = []
pesos = []
# Passo 1.3 Enquanto numero > 0 leia a lista dos números e pesos
while numero > 0:
# Passo 1.3.1. Leia o peso do boi i
    peso = float(input())
# Passo 1.3.2. Atribua número e peso a numeros[i] e pesos[i]
    numeros.append(numero)
    pesos.append(peso)
# Passo 1.3.3. Conte o número de bois
    numbois +=1
# Passo 1.3.4. Some o peso[i] 
    soma+=peso
# Passo 1.3.5. Leia o número do boi i+1
    numero = float(input())
# Passo 2. Compute os números e pesos dos dois bois com maior e menor peso
tam = len(numeros)
#Passo 2.1. Para os gordos
for i in range(0, tam):
    if maiorpeso < pesos[i]:
        maiorpeso2 = maiorpeso
        gordo2 = gordo1
        maiorpeso = pesos[i]
        gordo1 = numeros[i]
    if pesos[i] < maiorpeso and pesos[i] >= maiorpeso2:
        maiorpeso2 = pesos[i]
        gordo2 = numeros[i]
#Passo 2.2. Para os magros
    if menorpeso > pesos[i]:
        menorpeso2 = menorpeso
        magro2 = magro1
        menorpeso = pesos[i]
        magro1 = numeros[i]
    if pesos[i] > menorpeso and pesos[i] <= menorpeso2:
        menorpeso2 = pesos[i]
        magro2 = numeros[i]

# Passo 3. Calcule a média dos pesos dos bois
media = soma / tam
# Passo 4. Imprima os resultados
# Passo 4.1. Imprima a média dos pesos dos bois
print('Média dos pesos de ', end='')
print('{0:.0f} bois = {1:7.2f} Kg'.format(numbois, media))
# Passo 4.4 Imprima o número do boi mais magro e seu peso
print('Boi mais magro 1 = ', end = '')
print('{0:.0f} - Peso = {1:7.2f} Kg'.format(magro1,menorpeso))
# Passo 4.5 Imprima o número do segundo boi mais magro e seu peso
print('Boi mais magro 2 = ', end = '')
print('{0:.0f} - Peso = {1:7.2f} Kg'.format(magro2,menorpeso2))
# Passo 4.2 Imprima o número do boi mais gordo e seu peso
print('Boi mais gordo 1 = ', end='')
print('{0:.0f} - Peso = {1:7.2f} Kg'.format(gordo1,maiorpeso))
# Passo 4.3. Imprima o número do segundo boi mais gordo e seu peso
print('Boi mais gordo 2 = ', end = '')
print('{0:.0f} - Peso = {1:7.2f} Kg'.format(gordo2,maiorpeso2))


# pós: media == soma/numbois and soma == Soma i em
#      {0..numbois-1}:peso[i] and 
#      maiorPeso1 == peso[j] and maiorPeso2 == peso[k] and
#      para i em {0..numbois-1}:peso[j] >= peso[k] >= peso[i]
#      and gordo1 == numero[j] and gordo2 == numero[k] and
#      menorPeso1 == peso[l] and menorPeso2 == peso[r] and
#      para i em {1..numbois-1}:peso[l] =< peso[r] =< peso[i]
#      and magro1 == numero[l] and magro2 == numero[r]
# fim do módulo principal