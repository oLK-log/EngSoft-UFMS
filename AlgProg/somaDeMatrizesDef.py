# -*- coding: utf-8 -*-
# Programa: somaDeMatrizesDef.py
# Programador: Lorran Kaique
# Data: 08/07/2025
# Este programa a partir de 2 matrizes, deseja uma nova matriz com a soma
# resultante das duas
# pre= duas matrizes de mesmo tamanho
#pos= 1 unica matriz com mesmo tam das originarias
#Passo 0. Definir abstracoes
#int m, n
#list a,b,c
#Passo 0.1 cria funcoes
def somamat(m,n,a,b,c):
    #mn-dimensões matrizes
    #abc-matrizes
    for i in range(m):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c
#Passo 0.2 Inicializar variaveis
contab = 0
cont = 0
#Passo 1. Ler dados
#Passo 1.1 ler os tamanho m-linhas n -coluna
m, n = map(int, input().split())
#Passo 1.1.1 Inicializar variaveis dependentes
a = [[0 for _ in range(n)] for _ in range(m)]
b = [[0 for _ in range(n)] for _ in range(m)]
c = [[0 for _ in range(n)] for _ in range(m)]
#Passo 1.2 Ler os valores das matrizes
#Passo 1.2.1 Para a
for i in range(m):
    n1, n2 = map(int,input().split())
    for x in range(n):
        if cont == 0:
            a[i][x] = n1
            cont = 1
        else:
            a[i][x] = n2
            cont = 0
#Passo 1.2.2 Para b
for i in range(m):
    n1, n2 = map(int,input().split())
    for x in range(n):
        if cont == 0:
            b[i][x] = n1
            cont = 1
        else:
            b[i][x] = n2
            cont = 0
#Passo 3. Somar as matrizes
c = somamat(m,n,a,b,c)
#Passo 4. Imprimir matriz resultante
print(c)
