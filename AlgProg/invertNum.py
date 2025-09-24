# -*- coding: utf-8 -*-
# Programa: invertenum1.py
# Programador: Lorran Kaíque Silveira Fernandes
# Data: 26/04/2025
# Este programa que lê um número inteiro de quatro dígitos 
# num = d_3d_2d_1d_0 onde 0 indica a posição das unidades, 1 a das 
# dezenas, 2 a das centenas e 3 a dos milhares
# (num =  d_2*10^2 + d_1*10^1 + d_0*10^0).
# O seu programa deve inverter a ordem dos dígitos de num e gerar o
# numinvertido = d_0d_1d_2d_3 e imprimir o resultado.

# Passo 1. Leia os números
num = input()
# Passo 2. Inverta o número lido
n = len(num)
numinv = " "
num = int(num)
for i in range(0, n, 1):
    digito = num % 10
    numinv += str(digito)
    num = num // 10  
numinv= int(numinv)

# Passo 3. Imprima o número invertido
print('{0:d}'.format(numinv))