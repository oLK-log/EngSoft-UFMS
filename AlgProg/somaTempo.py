# -*- coding: utf-8 -*-
#Questao 2 lista
# Programa: somaTempo.py
# Programador: Lorran Kaíque Silveira Fernandes
# Data: 26/04/2025
# Este programa le duas horas decorridas, dadas em minutos e
# segundos e efetua a soma dessas duas medidas.
#Passo 1. Ler a entrada
d1, h1, m1, s1 = map(int, input().split())
d2, h2, m2, s2 = map(int, input().split())
#Passo 2. Calcule a soma dos tempos
#Passo 2.1. Calcule a soma total em segundos
total = s1 + s2 + m1*60 + m2*60 + h1*60*60 + h2*60*60 + d1*24*60*60 + d2*24*60*60
#Passo 2.2. Calcule a soma dos segundos
s = total % 60
total = total // 60
#Passo 2.3. Calcule a soma dos minutos
m = total % 60
total = total // 60
#Passo 2.4 Calcule a soma das hora
h = total % 24
#Passo 2.5 Calcule a soma dos dias
d = total // 24

#Passo 3. Imprima o resultado
print('{0:2d} Dias {1:2d} Horas {2:2d} Minutos {3:2d} Segundos +'.format(d1, h1, m1, s1))
print('{0:2d} Dias {1:2d} Horas {2:2d} Minutos {3:2d} Segundos ='.format(d2, h2, m2, s2))
print('{0:2d} Dias {1:2d} Horas {2:2d} Minutos {3:2d} Segundos'.format(d, h, m, s))