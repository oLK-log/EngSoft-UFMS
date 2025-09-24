# -*- coding: utf-8 -*-
# Programa: pantaneira.py
# Programador: lorran kaique
# Data: 21/05/25
# Este programa deve retornar o valor de um produto, dada o numero do produto
#e tendo duas listas de entrada(numeros e valores)
#entradas: list numero, valor. int cod
#saidas: float v
#Passo 0: Inicializar variaveis
ref = -1
#Passo 1: Ler as listas e cod
numero = list(map(int, input().split()))
valor = list(map(float, input().split()))
cod = int(input())
#Passo 2: Achar o indice do valor na lista
tam = len(numero)
for i in range(0,tam):
    if cod == numero[i]:
        ref = i
if ref == -1:
    resp = 'produto inexistente'
else:
    resp = valor[ref]
#Passo 3: Imprimir
print(resp)
