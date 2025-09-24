# -*- coding: utf-8 -*-
# Programa: randint00.py
# Programador:
# Data: 02/05/2017
# Programa para demonstrar a utilização da função randint(a,b)
# para gerar um série de números inteiros pseudo-aleatórios.
# início do módulo principal
# módulos utilizados
import random
# descrição das variáveis utilizadas
# int num1, num2, num3

# pré: semente

# Passo 1. Gere três números pseudo aleatórios
# Passo 1.1. Leia a semente
random.seed(int(input()))
# Passo 1.2. Gere três números inteiros no intervalo [0,100]
num1 = random.randint(0,100)
num2 = random.randint(0,100)
num3 = random.randint(0,100) 
# Passo 3. Imprima os números pseudo aleatórios
print('{0:d}'.format(num1))
print('{0:d}'.format(num2))
print('{0:d}'.format(num3))

# pós:  num1, num2, num3 && num[i] é um número pseudo aleatório
# fim do módulo principal