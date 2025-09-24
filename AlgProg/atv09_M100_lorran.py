# -*- coding: utf-8 -*-
# Programa: totalsegundos02.py
# Programador:
# Data: 17/05/2016
# Este programa lê uma medida de tempo, dada em dias, horas, 
# minutos e segundos e calcula seu equivalente em segundos.
# início do módulo principal
# descrição das variáveis utilizadas
# int dias, horas, minutos, segundos

# pré: dias, horas, minutos, segundos, totalsegundos 

# Passo 1. Leia a entrada
#(tem que ser na mesma linha?Caso sim, usa-se .sprit(' ') para separa-las)
print('Entre com a quantidade de dias, horas, minutos, segundos')
dias = int(input())
horas = int(input())
minutos = int(input())
segundos = int(input())
# Passo 2. Calcule o total de segundos
totalSegundos = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos
# Passo 3. Imprima o total de segundos
print('{0:d} Dias + {1:d} Horas + {2:d} Minutos + {3:d} Segundos = {4:d} Segundos'.format(dias, horas, minutos, segundos, totalSegundos))

# pós: totalSegundos == 24*3600*dias+60*60*horas+60*minutos+segundos
# fim do módulo principal