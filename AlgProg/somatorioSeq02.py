# -*- coding: utf-8 -*-
# Programa: somatoria01.py
# Programador:lk
# Data: 12/04/2025
# Este algoritmo calcula a soma dos n termos sequência
# S = 0/1 + 1/4 + 8/9 + 27/16 + ...
# início do módulo principal
# descrição das variáveis utilizadas
# int num, numerador, denominador
# float termo, soma

# pré: num > 0

# Passo 1. Leia o número de termos e inicialize soma
num = int(input())
soma = 0.00
# Passo 2. Calcule a soma dos n termos
# Passo 2.1. Compute
#numerador = (i - 1)**3
#denominador = (i*i)

for i in range(1,num+1):
    soma += (((i-1)**3)/(i*i))


# Passo 3. Imprima o valor da soma
print('{0:.6f}'.format(soma))

# pós: soma == Soma i em {1,...,num+1}: termo[i] and
#      termo[i] == (i-1)**3/(i**2)
# fim do módulo principal