# -*- coding: utf-8 -*-
# Programa: codifica00.py
# Programador: Lorran Kaíque Silveira Fernandes
# Data: 26/04/2025
#Dado 4 numero reais, obter a variancia, o desvio padrao e a media
#entrada: float n1, n2, n3, n4
#saida: float media, variancia, desvioP
#Passo 1- Ler notas
n1, n2, n3, n4 = map(float, input().split())
#Passo 2- Calcular a media
media = (n1 + n2 + n3 + n4 )/4
#Passo 3- calcular a variancia
#Passo 3.1 - Calcular os desvios
d1 = (n1 - media)**2
d2 = (n2 - media)**2
d3 = (n3 - media)**2
d4 = (n4 - media)**2
desvio = d1 + d2 + d3 + d4
#Passo 3.2 - Calcular a variância
variancia = desvio / 4
#Passo 4 - Calcular o desvio padrão
desvioP = variancia**(1/2)
# Passo 5 -  Imprima os resultados
print('Primeira Prova    {0:4.1f}'.format(n1))
print('Segunda Prova     {0:4.1f}'.format(n2))
print('Terceira Prova    {0:4.1f}'.format(n3))
print('Quarta Prova      {0:4.1f}'.format(n4))

print('Média das Provas {0:6.2f}'.format(media))
print('Variância        {0:6.2f}'.format(variancia))
print('Desvio Padrão    {0:6.2f}'.format(desvioP))
