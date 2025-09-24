# -*- coding: utf-8 -*-
# Programa: randange00.py
# Programador:
# Data: 01/05/2020
# Programa para demonstrar a utilização da função randrange()
# para gerar uma lista de 10 números inteiros pares pseudo 
# aleatórios, entre 100 e 999.
# início do módulo principal
# declaração dos módulos utilizados
import random
# descrição das variáveis utilizadas
# list pares
# int semente, numero

# pré: semente

# Passo 1. Leia a semente e inicialize a sequência
semente = int(input())
random.seed(semente)
# Passo 2. Gere a lista de números pares
# Passo 2.1. Inicialize a lista
pares = []
# Passo 2.2. Gere 10 números pares
for i in range(0,10):
# Passo 2.2.1. Gere o i-ésimo numero
   numero = random.randrange(100,1000,2)
# Passo 2.2.2. Insira numero na lista
   pares.append(numero)
# Passo 3. Imprima a lista
print(pares)

# pós: pares and para i im {0..9}:pares[i] em [0,1000) and
#      pares[i]%2 == 0
# fim do módulo principal