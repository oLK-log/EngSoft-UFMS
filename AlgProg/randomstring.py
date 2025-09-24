# -*- coding: utf-8 -*-
# Programa: randomstring.py
# Programador:
# Data: 01/05/2020
# Programa para demonstrar a geração de strings aleatórias.
# O programa lê um inteiro num e gera uma string aleatória
# com num caracteres latinos e imprime o resultado.
# início do módulo principal
# declaração dos módulos utilizados
import random
import string
# descrição das variáveis utilizadas
# string palavra, alfabeto, letra
# int semente, num

# pré: num semente

# Passo 1. Leia a entrada
# Passo 1.1. Leia o número de caracteres
num = int(input())
# Passo 1. Leia a semente
semente = int(input())
random.seed(semente)
# Passo 2. Gere uma string com num caracteres
# Passo 2.1. Inicialize o alfabeto
alfabeto = string.ascii_letters
# Passo 2.2. Inicialize a palavra
palavra = ''
# Passo 2.2. Gere a string
for i in range(0,num):
# Passo 2.2.1. Gere o i-ésimo caractere
   letra = random.choice(alfabeto)
# Passo 2.2.2. Insira a letra na palavra
   palavra = palavra + letra
# Passo 3. Imprima a palavra
print(palavra)

# pós: palavra and palavra[i] é um caractere aleatório
# fim do módulo principal