# -*- coding: utf-8 -*-
# Programa: maxfatorPO.py
# Programador: Lorran Kaíque
# Data: 06/07/2025
# Este programa define e utiliza a função maxfator() para computar
# o maior fator de um dado inteiro que seja menor que o próprio número.
#Funcionamento da função: além de tratar os casos especiais, é preciso percorrer
#o n de tras pra frente, pois deseja-se o maior numero < que n.
#Além disso, o maior numero divisor menor que n nunca vai ser maior que a metade de n
#Passo 0. Abstrações
#Passo 0.1 Definir funcões
def maxfator(numero):
    #Essa funcao computa o maior fator de um dado inteiro |n| que seja menor que |n|.
    #Regras especiais:
    #- Para |n|=0 ou |n|=1, o maior fator é definido como |n|.
    #- Para números primos, o maior fator é 1.
    n = abs(numero)#Lidar com o valor absoluto
    if n == 0 or n == 1:#Casos especiais
        return n
    #Buscar o maior fator de trás para frente.
    # Um fator (que não seja o próprio número) nunca será maior que n/2.
    for i in range(n // 2, 0, -1):
        # se o resto == 0, ent é o maior fator
        if n % i == 0:
            return i
    #Se não encontrar nengum valor
    return 1
#Passo 1. receber o valor
entry = int(input())
#Passo 2. Encontrar ser maxfator
fatorMax = maxfator(entry)
#Passo 3 imprimir
print(f"{entry} {fatorMax}")