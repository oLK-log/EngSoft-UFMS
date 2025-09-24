# -*- coding: utf-8 -*-
# Programa: energizadorParticulas
# Programador: Lorran Kaíque
import time
inicio = time.time()
#Este programa
#A particula começa em x com carga Y
# ela absorve a energia k vezes, ela se move uma distancia igual a o mdc de (x,y)
#entrada: int Y, K
#saída: int posFinal
#Iniciar funções
#funcao mdc
def mdc(a, b):
    while b:
        resto = a % b
        a = b
        b = resto
    return a
#Passo 0: Iniciar variaveis
posAtual = 1#a posição inicia em 1
#Passo 1: Receber entradas
y, k = map(int,input().split())
#Passo 2:iterar
#vai uterar k vezes
for _ in range(k):
    posAtual += mdc(posAtual, y)
#Passo 3: Imprimir o resultado com nenhuma casa decimal
print('{0:d}'.format(posAtual))

fim = time.time()
tempo = fim - inicio
print(tempo)
    