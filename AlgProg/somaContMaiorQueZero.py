# -*- coding: utf-8 -*-
# Programa: contapos.py
# Programador:lk
# Data: 15/04/25
# Este programa lê quatro números inteiros, conta quantos números positivos
# foram lidos e imprime o resultado.
# início do módulo principal
# descrição das variáveis utilizadas
# int num1, num2, num3, num4
# int numpos, somapos

# pré: num1 num2 num3 num4
contador = 0
soma = 0
# Passo 1. Leia 4 números inteiros
entr = input()
num1, num2, num3, num4= entr.split(" ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = int(num4)
# Passo 2. Calcule o numero e a soma de positivos
# Passo 2.1. Inicialize numpositivos e soma
if num1 > 0:
    soma += num1
    contador += 1
if num2 > 0:
    soma += num2
    contador += 1
if num3 > 0:
    soma += num3
    contador += 1
if num4 > 0:
    soma += num4
    contador += 1
    
# Passo 2.2. Compute o numero e a soma dos positivos 	

# Passo 3. Imprima os resultados
print("Número de positivos lidos: {0:d}\nSoma dos números positivos: {1:d}".format(contador, soma))

# pós: numpos == Num i em {1,..4}: num[i] > 0 and
#      somapos == Soma i em {1...4}: num[i] and num[i] > 0 
# fim do módulo principal