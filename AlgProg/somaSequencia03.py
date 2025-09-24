# -*- coding: utf-8 -*-
# Programa: somatoria22.c
# Programador:
# Data: 12/10/2013
# Este programa lê um valor de X e n e calcula a soma dos n primeiros termos
# S = 1 - X^2/3! + X^4/5! - X^6/7! + ...
# O primeiro termo da série é 1 o segundo é 1 * -((X * X)/(1 * 2 * 3))
# o terceiro termo é (o segundo) -X^2/3! * - ((X*X)/(4 * 5))
# de forma geral é o termo anterior * -((X*X)/((2*i)*(2*i+1)))
# onde i é o termo da série
# Declaração das bibliotecas utilizadas
import math

# início 

# pré: UmFloat && UmFloat == A

# Passo 1. Leia a entrada
# Passo 1.1. Leia o valor de x
#   print('Leia o valor de x: ')
x = float(input())
# Passo 1.2. Leia o número de termos
#   print('Leia o número de termos: ')
num = int(input())
i = 0.0
soma= 1.0
inversor = 1.0
# Passo 2. Calcule o valor da somatória
for a in range(1, num):
    i +=2
#numerador = (x**i)
    numerador = (x**i)
#denominador = (i+1)!
    b = (i+1)
    denominador = (i+1)
    while 1 < b:
        b -= 1
        denominador *= b
#sum = numerador / denominador
    inversor *= -1
    soma += inversor * (numerador/denominador)
if num == 1:
    soma = 1.0
# Passo 3. Imprima o valor da somatória
print('Soma({0:+.4f}) = {1:+.6f}'.format(x, soma))

# pós: Soma == Soma i em {0,...,5}: termo && termo == X^{2i}/(2i+1)!
# fim