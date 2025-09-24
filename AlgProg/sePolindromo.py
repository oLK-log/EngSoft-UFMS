# -*- coding: utf-8 -*-
# Programa: palindromo.py
# Programador: lorran kaíque Silveira Fernandes
# Data: 28/04/2025
# Este programa lê um número inteiro, indicando a 
# quantidade de números a serem lidos. O programa le cada
# um dos números e a cada número lido computa se ele é
# palíndromo.
# início do módulo principal
# descrição das variáveis utilizadas
# int numero, num, reverso, digito

# pré: num == d[k]d[k-1]...d[1]d[0]

# Passo 1. Leia o número e inicialize as variáveis
# Passo 1.1. Leia o número
num = int(input())
polindromo = True
#Passo 2- limitaçoes
if num < 10:#n com menos de 2 digitos
    polindromo = False
elif num < 0:#n negativos
    polindromo = False
#Passo 4- fzr a log principal
else:
    var_num = num
    potencia = 1
    #definindo a potencia
    while var_num // 10 > 0:
        var_num //= 10
        potencia *= 10
        
    while num > 0:
        primeiroDig = num // potencia
        ultimoDig = num % 10
        
        if primeiroDig != ultimoDig:
            polindromo = False
            break
        
        num %= potencia
        num //= 10
        potencia //= 100
        
        if num < 10 and num >= 0:
            break
if polindromo == True:
    msg='sim'
else:
    msg='não'
# Passo 4. Imprima a resposta
print('{0}'.format(msg))

# pós: (sim and d[k]d[k-1]...d[1]d[0] == d[0]d[1]...d[k-1]d[k]) or não
# fim do módulo principal
