# -*- coding: utf-8 -*-
# Programa: maxfatorDef.py
# Programador: Lorran Kaique
# Data: 06/07/2025
# Este programa usa a funcao maxfator() para computar o maior
#fator de um dado inteiro N>1 que seja menor que o próprio n
#obs: fatores são divisores
#Passo 0. Inicializar abstracoes
#def maxfator
#int entry, start
#Passo 0.1 inicializar funcoes
def maxfator(n):
    #Essa funcao computa o maior fator de um dado numero n que seja menor
    #que n
    #Regras: - para n = 0, ou n = 1 o maior fator é n
    #- para numeros primos o maior fator é 1
    #pegando valor absoluto
    num = abs(n)
    #Excessão 0 e 1
    if num == 0 or num == 1:
        return num
    #O maior fator de n que não seja ele próprio nunca seja maior que n/2   
    start = n//2
    for i in range(start, 0, -1):
        if n % i == 0:
            return i
    #quando nada é encontrado é 1
    return 1
#Passo 1. Ler a entrada
entry =int(input())
#Passo 2. Impprimir
print(entry, maxfator(entry))