# -*- coding: utf-8 -*-
# Programa: somaMatrizPO.py
# Programador: Lorran Kaíque
# Data: 11/07/2025
# Este programa le dois numeros m e n que equivalem a linha e coluna de uma matriz
#Ele recebe os valores da matriz e então
# ele gera uma nova matriz que equivale a soma das mesmas posicoes equivalente nas matrizes base
#Funcionamento: primeiro o programa lê o numero de coluna e linha(m,n)
#A partir desses numeros, o programa cria as matrizes vazias a, b e c
#para a e b criamos apenas as linhas, pois a entrada é feita com dois valores de uma vez
#Pra c é preciso criar a matriz completa (mXn)
#A soma é feita usando indicadores de posições i e j que indicarao a posicao em c
#(que é a mesma em a e b) que a na mesma posicao devera ser somado ao b na mesma posicao
#Passo 0. Abstracoes
#Passo 1. receber inf do usuario
#Passo 1.1 ler dimensões
m, n = map(int, input().split())
#Passo 1.1.1 Inicializar matrizes
a = [[] for _ in range(m)]
b = [[] for _ in range(m)]
c = [[0 for _ in range(n)] for _ in range(m)]
#Passo 1.2 ler a matriz
for i in range(m):
    a[i] = list(map(int, input().split()))
for i in range(m):
    b[i] = list(map(int, input().split()))
#Passo 2. somar as matrizes em "a" e "b" e colocar em "c"
for i in range(m):
    for j in range(n):
        c[i][j] = a[i][j] + b[i][j]
#PAsso 3, Imprimir as matrizes
for linha in c:
    print(linha)
        