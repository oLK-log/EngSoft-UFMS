# -*- coding: utf-8 -*-
# Programa: varianciaProvasDef.py
# Programador: Lorran Kaique
# Data: 06/07/2025
# Este programa le 4 notas e imprime a media, variancia
#e desvio padrao
#importacoes
import math
#Passo 0.Inicializar abstracoes
#Passo0.1 funcoes
def mediaProva(listaNotas):
    totalNotas=0
    for nota in listaNotas:
        totalNotas+=nota
    media = totalNotas/4
    return media
def varianciaNotas(media,listaNotas):
    #v=(somatorio(nota-media)²)/n
    somatorio=0
    for nota in listaNotas:
        somatorio+= ((nota-media)**2)
        variancia = somatorio/4
    return variancia
def desvioPadraoNotas(variancia):
    desvioP= math.sqrt(variancia)
    return desvioP
    
#Passo1. Ler valores
listaNotas = list(map(float,input().split()))
#Passo 2. Calcular a media
media = mediaProva(listaNotas)
#Passo 3. Calcular a variancia
variancia = varianciaNotas(media, listaNotas)
#Passo 3. Calcular o desvio Padrao
desvioP = desvioPadraoNotas(variancia)
#Passo 4. Imprimir resultados
print('Primeira Prova    {0:4.1f}'.format(listaNotas[0]))
print('Segunda Prova     {0:4.1f}'.format(listaNotas[1]))
print('Terceira Prova    {0:4.1f}'.format(listaNotas[2]))
print('Quarta Prova      {0:4.1f}'.format(listaNotas[3]))

print('Média das Provas {0:6.2f}'.format(media))
print('Variância        {0:6.2f}'.format(variancia))
print('Desvio Padrão    {0:6.2f}'.format(desvioP))