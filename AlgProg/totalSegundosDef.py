# -*- coding: utf-8 -*-
# Programa: totalSegundosDef.py
# Programador: Lorran Kaique
# Data: 06/07/2025
# Este programa a partir de uma entrada horas,minutos,segundos
#calcular a quantidade total de segundos
#def converterEmSegundo
#Passo 1. Criar def
def converterEmSegundo(hr,mn,seg):
    total = (hr*60*60) + (mn*60) + seg
    return total
#Passo 2. Ler entrada
hr, mn, seg = map(int, input().split())
#Calcular total
tSeg = converterEmSegundo(hr, mn, seg)
#Passo 3. Imprimir
print(tSeg)