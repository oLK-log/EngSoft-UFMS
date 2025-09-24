# -*- coding: utf-8 -*-
# Programa: somatorioAlturas.py
# Programador: lORRAN kAÍQUE
# Data: 05/05/2025
# Este programa le um conj de alturas, armazena em uma lista
# calcula a media e imprime a media e o numero de alturas maiores ou iguais a media
#Entradas: list alt
#saidas: float media, alturasMaiores
#Passo 0: Iniciar variaveis
alt = 1
media = 0
contador = 0
alturas = []
alturasMaiores = []
#Passo 1: Ler em cada linha e add a lista
while alt != 0.0:
    alt = float(input())
    alturas.append(alt)
#Passo 2> CAlcular a média das alturas    
for i in range(0, len(alturas), 1):
    media += alturas[i]
    contador+=1
media /= (contador-1)
#Passo 3- salvar valores maiores ou iguais a media
for i in range(0, len(alturas), 1):
    if alturas[i] >= media:
        alturasMaiores.append(alturas[i])
#Passo 4- Imprimir media e alturasMaiores
print('{0:.2f}'.format(media))
print(len(alturasMaiores))
    