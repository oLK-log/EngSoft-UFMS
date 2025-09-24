# -*- coding: utf-8 -*-
# Programa: emaranhamento
# Programador: Lorran Kaíque
#Este programa
#Passo 0: iniciar variaveis
info = []
resp = -1
#Passo 1 Ler entradas
#Passo 11. ler N e T
n, t = map(int, input().split())
#Passo 1.2. Ler informacoes
for i in range(0, n):
    info.append(list(map(int,input().split())))
#Passo 1.3: Ler L e U (min e max de tempo que o sensor pode ficar atv)
min = int(input())
max = int(input())
