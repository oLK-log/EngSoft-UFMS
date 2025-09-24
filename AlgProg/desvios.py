# -*- coding: utf-8 -*-
# Programa: desvios.py
# Programador: lORRAN kAÍQUE
# Data: 05/05/2025
# Este programa, a partir de uma lista, calcula a media, a variancia e o desvio padrao
#entradas:
#int n-se refere a qt de elem da lista
#list lista
#saida: float media, variancia, desvioP
#Passo 0: iniciar variaveis
media = 0
variancia = 0
#Passo 1: Ler n elementos da lista e lista
n = int(input())
lista = list(map(float, input().split()))
#Passo2: calcular a media
for i in range(0, len(lista), 1):
    media += lista[i]
media /= n
#Passo 3: calcular a variancia
for i in range(0, len(lista), 1):
    variancia += ((lista[i]-media)**2)
variancia /= n
#Passo 4: calcular o desvio padrao
desvioP = (variancia**(1/2))
#Passo 5: imprimir media, variancia e desvio Padrao
print('Média ={0:6.2f}'.format(media))
print('Variância ={0:6.2f}'.format(variancia))
print("Desvio Padrão ={0:6.2f}".format(desvioP))