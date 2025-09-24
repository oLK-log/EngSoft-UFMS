# Programa: caracteres.py
# Programador:
# Data: 09/08/2022
# Este programa lê uma strin de caracteres visíveis sem o 
# caracter espaço e computa e imprime o primeiro e o
# último caractere da palavra lida.
# início do módulo principal
# descrição das variáveis utilizadas
#include<stdio.h> // printf
# str palavra, primeiro, ultimo

# pré: palavra == c[0]c[1]...c[tam-1]

# Passo 1. Leia uma palavra
palavra = input()
# Passo 2. Calcule o primeiro e o último caractere da palavra
nPal = len(palavra)
# Passo 2.1. Calcule o primeiro caractere da palavra
i = 1
for letra in palavra:
    if i == 1:
        primeira = letra
    if i == nPal:
        ultima = letra
    i +=1
# Passo 2.2. Calcule o último caractere da palavra

# Passo 3. Imprima os resultados
print(primeira, ultima)

# pós: c[0] c[tam-1]
# fim do módulo principal
