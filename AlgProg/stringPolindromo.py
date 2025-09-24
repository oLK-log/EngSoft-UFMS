# -*- coding: utf-8 -*-
# Programa: palindromo.py
# Programador: lorran kaíque Silveira Fernandes
# Data: 28/04/2025
entrada = input()
string_sem_espacos = ""

for caractere in entrada:
    if caractere != ' ':
        string_sem_espacos = string_sem_espacos + caractere

palavra = string_sem_espacos
palavra_reversa = ""
indice = len(palavra) - 1

while indice >= 0:
    caractere = palavra[indice]
    palavra_reversa = palavra_reversa + caractere
    indice = indice - 1

if palavra == palavra_reversa:
    print("palíndromo")
else:
    print("não palíndromo")