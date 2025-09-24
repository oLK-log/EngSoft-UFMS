# -*- coding: utf-8 -*-
# Programa: cifrador01.py
# Programador:
# Data: 27/04/2016
# Este programa lê uma palavra composta por 5 caracteres visíveis e um
# número inteiro no intervalo [0,25]. O programa codifica os caracteres da
# palavra que pertencem ao alfabeto {'A',..,'Z','a',..,'z'} usando o
# deslocamento dos caracteres da string de entrada. Os caracteres do
# alfabeto são tratados de forma circular, ou seja, 'Z' + 1 == 'A' e
# 'z' + 1 == 'a'. Os demais caracteres permanecem inalterados. A codificação 
# da palavra é feita usando os códigos ASCII dos caracteres. O programa
# imprime a palavra codificada.
# início do módulo principal
# Descrição das variáveis utilizadas
# str palavra, codificada
# str char0, char1, char2, char3, char4
# deslocamento
# pré: palavra deslocamento and palavra[i] caractere visível
# Passo 1. Leia uma palavra com 5 caracteres visíveis e o deslocamento
# Passo 1.1. Leia uma palavra com 5 caracteres visíveis
palavra = str(input())
# Passo 1.2. Leia o deslocamento
codificador = int(input())
# Passo 2. Codifique os caracteres da palavra
# Passo 2.1. Codifique o primeiro caractere
# Passo 2.1.1. Se o caractere for do alfabeto maiúsculo
if palavra[0].isupper():
# Passo 2.1.1.1. Codifique o caractere
   char0 = chr((ord(palavra[0]) - ord('A') + codificador)%26 + ord('A'))
# Passo 2.1.2. Se o caractere for do alfabeto minúsculo
elif palavra[0].islower():
# Passo 2.1.2.1. Codifique o caractere
   char0 = chr((ord(palavra[0]) - ord('a') + codificador)%26 + ord('a'))
# Passo 2.1.3. Se o caractere não for do alfabeto
else:
# Passo 2.1.3.1. Mantenha o caractere
   char0 = palavra[0]
# Passo 2.2. Codifique o segundo caractere
# Passo 2.2.1. Se o caractere for do alfabeto maiúsculo
if palavra[1].isupper():
# Passo 2.2.1.1. Codifique o caractere
   char1 = chr((ord(palavra[1]) - ord('A') + codificador)%26 + ord('A'))
# Passo 2.2.2. Se o caractere for do alfabeto minúsculo
elif palavra[1].islower():
# Passo 2.2.2.1. Codifique o caractere
   char1 = chr((ord(palavra[1]) - ord('a') + codificador)%26 + ord('a'))
# Passo 2.2.3. Se o caractere não for do alfabeto
else:
# Passo 2.2.3.1. Mantenha o caractere
   char1 = palavra[1]   
# Passo 2.3. Codifique o terceiro caractere
# Passo 2.3.1. Se o caractere for do alfabeto maiúsculo
if palavra[2].isupper():
# Passo 2.3.1.1. Codifique o caractere
   char2 = chr((ord(palavra[2]) - ord('A') + codificador)%26 + ord('A'))
# Passo 2.3.2. Se o caractere for do alfabeto minúsculo
elif palavra[2].islower():
# Passo 2.3.2.1. Codifique o caractere
   char2 = chr((ord(palavra[2]) - ord('a') + codificador)%26 + ord('a'))
# Passo 2.3.3. Se o caractere não for do alfabeto
else:
# Passo 2.3.3.1. Mantenha o caractere
   char2 = palavra[2]   
# Passo 2.4. Codifique o quarto caractere
# Passo 2.4.1. Se o caractere for do alfabeto maiúsculo
if palavra[3].isupper():
# Passo 2.4.1.1. Codifique o caractere
   char3 = chr((ord(palavra[3]) - ord('A') + codificador)%26 + ord('A'))
# Passo 2.4.2. Se o caractere for do alfabeto minúsculo
elif palavra[3].islower():
# Passo 2.4.2.1. Codifique o caractere
   char3 = chr((ord(palavra[3]) - ord('a') + codificador)%26 + ord('a'))
# Passo 2.4.3. Se o caractere não for do alfabeto
else:
# Passo 2.4.3.1. Mantenha o caractere
   char3 = palavra[3]
# Passo 2.5. Codifique o quinto caractere
# Passo 2.5.1. Se o caractere for do alfabeto maiúsculo
if palavra[4].isupper():
# Passo 2.5.1.1. Codifique o caractere
   char4 = chr((ord(palavra[4]) - ord('A') + codificador)%26 + ord('A'))
# Passo 2.5.2. Se o caractere for do alfabeto minúsculo
elif palavra[4].islower():
# Passo 2.5.2.1. Codifique o caractere
   char4 = chr((ord(palavra[4]) - ord('a') + codificador)%26 + ord('a'))
# Passo 2.5.3. Se o caractere não for do alfabeto
else:
# Passo 2.5.3.1. Mantenha o caractere
   char4 = palavra[4]
   
#Passo 2.6 Codifique o sexto caractere
if palavra[5].isupper():
# Passo 2.6.1.1. Codifique o caractere
    char5 = chr((ord(palavra[5]) - ord('A') + codificador)%26 + ord('A'))
# Passo 2.6.2. Se o caractere for do alfabeto minúsculo
elif palavra[5].islower():
# Passo 2.6.2.1. Codifique o caractere
   char4 = chr((ord(palavra[5]) - ord('a') + codificador)%26 + ord('a'))
# Passo 2.6.3. Se o caractere não for do alfabeto
else:
# Passo 2.6.3.1. Mantenha o caractere
   char5 = palavra[5]
# Passo 2.6. Concatene os caracteres
codificada = char0 + char1 + char2 + char3+ char4 + char5
# Passo 3. Imprima a mensagem codificada
print('{0:s}'.format(codificada))
# pós: codificada and codificada[i] caractere visível and 
#      para i em {0,..,4}:codificada[i] == (palavra[i] + deslocamento
#      and palavra[i] em {'A',..,'Z','a',..,'z'} or 
#      or codificada[i] == palavra[i]
# fim do módulo principal