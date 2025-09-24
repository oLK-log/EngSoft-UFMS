# -*- coding: utf-8 -*-
# Programa: 
# Programador:Lorran Kaíque
# Data: 16/05/2025
# Este programa deve simular repetidamente o lançamento de uma moeda
#e para quando o resultado for cara
#n é o numero de sorteior e o premio equivale a 2.n
import random
#entradas: int semente
#variaveis: int total, numJog
#saída: float media
#Passo 0: Inicializar as variaveis
totalJogada = 0
numJog = 100
varControle = 0.0
premio = 0
#Passo 1: Ler semente
semente = int(input())
#Passo 1.2. Normalizar a semente
random.seed(semente)
#Passo 2: iterar jogadas
#Pensamento: usar 0 para indicar Coroa
#e 1 para indicar Cara
for i in range(10):
    n = 0
    while varControle == 0:        
        numAl = random.randint(0,1)
        n +=1
        totalJogada +=1
        if numAl == 1:
            premio += 2*n
            print(n, premio)
            varControle = 1
    varControle = 0
#Passo 3: Calcular média
mediaJ = premio/totalJogada
mediaIn = premio / 10
#Passo 4: Imprimir
print(totalJogada)
print(f"{mediaJ:.2f}")
print(f"{mediaIn:.2f}")