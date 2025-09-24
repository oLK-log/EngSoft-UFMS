# -*- coding: utf-8 -*-
# Programa: consumo1.py -- versão vpl
# Programador:
# Data: 30/05/2013
# Este programa lê um conjunto dois números representando a
# quantidade de quilômetros viajados e a quantidade de litros de
# combustível utilizado, respectivamente, por um dado veículo. O
# programa calcula e imprime a quantidade de quilômetros por litro 
# de combustível para cada veículo. Para todas médias de consumo, 
# o programa computa as duas piores médias de consumo (maior
# número de quilômetros rodados por litro de combustível).
#entrada: list frota
#saida: list ls
#Passo 0: iniciar variaveis
frota = []
ls = []
#Passo 1: Ler os valores
for i in range(1):
    frota.append(list(map(str,input().split())))
#Passo 3: adicionar orimeira coluna a nova lista
for i in range(1):
    ls.append(frota[i][0])
#Passo 4: calcular o gasto/km e add a nova lista
#Passo 4.1 Criar listas separadas para cada elemento
for i in range(1):
    km = frota[i][1].strip().split(' ')
    l = frota[i][2].strip().split(' ')
#Passo 4.2 Converter de str para float
km = [float(q) for q in km]
l = [float(tr) for tr in l]
for i in range(1):
    gasto = l[i] / km[i]
    ls[i][1] = str(gasto)
print(*ls)
#Passo 2: converter valores str ara float

#for i in range(1):
#    notas_str = conjuntoDados[i][2].strip().split(' ')
#    km = [float(quil) for quil in frota[i][2]]
