# -*- coding: utf-8 -*-
# Programa: matrizPascal.py
# Programador: Lorran Kaíque
# Data: 08/06/25
# Este programa dado um numero de entrada, deseja esse numero de linhas de Pascal
#Passo 0. Iniciar variáveis
sub = 0
valor = 1
#Passo 1. Ler n
n = int(input())
#Passo 2. Contruir matriz
matriz = []
for i in range(n):#linhaa
    linha = []
    for j in range(i+1):#coluna
        if j == 0 or j == i:
            valor = 1
        else:
           valor = matriz[i-1][j-1] + matriz[i-1][j]
        linha.append(valor)
    matriz.append(linha)

#Passo 3. Imprimir
for i in range(n):
    for j in range(i+1):
        numero = matriz[i][j]
        if numero != 0:
            print("{:4d}".format(numero), end="")
    print()