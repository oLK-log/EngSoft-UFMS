# -*- coding: utf-8 -*-
# Programa: randfloat01.py
# Programador:
# Data: 02/05/2017
# Programa para demonstrar a utilização da função random()
# para gerar um série de números float pseudo aleatórios
# no intervalo [min,max).
# início do módulo principal
# módulos utilizados
import random
# descrição das variáveis utilizadas
# float num1, num2, num3, minimo, maximo
# int semente

# pré: semente

# Passo 1. Gere três números pseudo aleatórios
# Passo 1.1. Leia a semente
semente = int(input())
# Passo 1.2. Leia os limites do intervalo
minimo = float(input())
maximo = float(input())
# Passo 2. Gere três números float em [minimo,maximo)
# Passo 2.1. Inicialize a sequência relativa a semente
random.seed(semente)
# Passo 2.2. Gere os números no intervalo [0,1)
num1 = random.random()
num2 = random.random()
num3 = random.random() 
# Passo 2.3. Translade os números para o intervalo [minimo, maximo)
num1 = minimo + (num1 * (maximo-minimo))
num2 = minimo + (num2 * (maximo-minimo))
num3 = minimo + (num3 * (maximo-minimo))
# Passo 3. Imprima os números pseudo aleatórios
print('{0:f}'.format(num1))
print('{0:f}'.format(num2))
print('{0:f}'.format(num3))

# pós:  num1, num2, num3 && num[i] é um número pseudo aleatório
# fim do módulo principal