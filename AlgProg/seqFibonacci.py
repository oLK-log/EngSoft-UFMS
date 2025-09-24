# -*- coding: utf-8 -*-
# Programa: fibonaci02.py
# Programador:lk
# Data: 16/04/25
# Este programa lê um inteiro positivo num > 1 e calcula e imprime
# os num termos da sequência de Fibonaci usando um algoritmo iterativo.
# declaração de módulos utilizados
# início do módulo principal
# descrição das variáveis utilizadas
# int num, fib1, fib2, novoFib

# pré: num > 0

# Passo 1. Leia um inteiro positivo
#o n de fibo é a soma dos dois anteriores
num = int(input())
fibAnt1= 1
fibAnt2= 0
print('{0:d} '.format(fibAnt1), end="")
for i in range(2,num+1,1):
    fib = fibAnt1 + fibAnt2
    print('{0:d} '.format(fib), end="")
    fibAnt2 = fibAnt1
    fibAnt1 = fib

# pós: num {fib[i] <= numero} | fib[1] == 1 && fib[2] == 1 && 
#      fib[i] == fib[i-2] + fib[i-1]
# fim do módulo principal