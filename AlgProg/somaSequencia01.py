# -*- coding: utf-8 -*-
# Programa: somasequencia01.py
# Programador:
# Data: 12/09/2010
# Este programa lê um número inteiro num, calcula a soma dos num
# termos da sequência S = 1 + 3/2 + 5/3 + 7/4 + ... + 99/50
# e imprime o resultado
# inicio do módulo principal
# descrição das variáveis utilizadas
# float soma, termo
# int num, den

# pré: num

# Passo 1. Leia o numero de termos  
print('Entre com o numero de termos: ')
num = int(input())
# Passo 2. Calcule a soma dos num termos da sequência
# Passo 2.1. Inicialize a soma
soma = 1.0
var = 1.0
for x in range(2,num+1):
    var = (2*x -1)
    soma += (var/x)
print("Soma : {0:.6f}".format(soma))
if num == 0:
    soma = 0.0
# Passo 3. Imprima o valor da soma
print('Soma : {0}'.format(soma))

# pós: soma == Soma i em {1..num}:termo[i] and
#      termo[i] == (2*i - 1)/i
# fim do módulo principal