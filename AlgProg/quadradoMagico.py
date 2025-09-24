# -*- coding: utf-8 -*-
# Programa: quadradoMagico.py
# Programador: Lorran Kaíque
# Data: 08/06/25
# Este programa constroi um quadrado magico n X n para um valor ímpar 0 < n <= 50
#Iniciar variaveis
mov = 1
#Passo 1 Receber o valor de n
n = int(input())
#Passo 1.2 Criar uma matriz vazia
matriz = [[0 for coluna in range(n)] for linha in range(n)]
#ou
#matriz = []
#for i in range(n):
    #linha = []*n
    #matriz.append(linha)
#Passo 2. Definir posição inicial de 1(centro)
inicia = 1 + ((n//2)-1)
#Passo 3. Adicionar 1 ao meio da primeira linha
matriz [0][inicia] = 1
#Passo 4. Movimentar 1 cima e 1 direita colocando K+1
linha = 0
coluna = inicia
for numero in range(2, n*n +1):
    lant= linha
    cant = coluna
    mov += 1
    coluna += 1
    linha -= 1
    if coluna >= n:
        coluna = 0
    if linha < 0:
        linha = n-1
    if matriz[linha][coluna] != 0:
        linha = lant + 1
        coluna = cant
    matriz[linha][coluna] = mov
#Passo 5, Imprimir Matriz
for i in range(n):
    print(matriz[i])