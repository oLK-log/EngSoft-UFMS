# -*- coding: utf-8 -*-
# Programa: seMaiorDef.py
# Programador: Lorran Kaique
# Data: 08/07/2025
# Este programa dada uma lista de numeros inteiros verifica se
#o primeiro numero da lista é maior que os demais. Se sim
# imprimi "sim", caso contrário, "não"
#pres: tem que ser numeros inteiros
#pros: str "sim" ou "nao"
#Passo 0. Definir abstrações
#Passo 0.1 definir funcoes
def ehMaior(L, tam):
    primeiro = L[0]
    for i in range(1, len(L)):
        if primeiro <= L[i]:
            return "não"
    return "sim"
#Passo 1. Ler entradas:
tam = int(input())
L = list(map(int, input().split()))
#Passo 2. Verificar se é o maior
resposta = ehMaior(L, tam)
#Passo 3. Imprimir resposta
print(resposta)