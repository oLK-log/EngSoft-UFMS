# -*- coding: utf-8 -*-
# Programa: fibonaci02.py
# Programador: lORRAN kAÍQUE
# Data: 05/05/2025
# Este programa lê um inteiro positivo num > 1 e calcula e imprime
# os num termos da sequência de Fibonaci usando um algoritmo iterativo.
# início do módulo principal
# descrição das variáveis utilizadas
# int num, fib1, fib2, novoFib

# pré: num > 0

# Passo 1. Leia um inteiro positivo
num = int(input())
# Passo 2. Calcule e imprima os num termos da sequênci
# Passo 2.1. Calcule o primeiro termo
fib1 =1
fib2 = fib1
print(fib1, fib2, end=" ")
for i in range(2, num, 1):
    novoFib = fib1 + fib2
    print('{0:d} '.format(novoFib),end='')
    fib2 = fib1
    fib1 = novoFib
# Passo 2.2. Imprima o primeiro termo
#print('{0:d} '.format(novoFib),end='')
# Passo 3. Gere e imprima os demais termos da sequência

# pós: para i em {1,...,num}: fib_i and fib_1 == 1 and 
#      fib_2 == 1 and fib_i == fib_(i-2) + fib_(i-1) and i >= 3
# fim do módulo principal
