# -*- coding: utf-8 -*-
# Programa: pisoLogDef.py
# Programador: Lorran Kaíque
# Data: 08/07/2025
#Este programa ao receber um numero inteiro >= 1, gera o piso logaritmos
#na base 2 do número de entrada
#inverter potenciacao
#log²(16)= 4 --> 16//2 = 8 (cont =1) --> 8//2 = 4(cont = 2) --> 4//2 = 2(cont = 3) --> 2//2 = 1 (cont=4)
#qunatas vezes divide por 2 até chegar a 1?
#Passo 0. Iniciar abstracoes
#Passo0.1 Iniciar funções
def piso_log(num):
    #Essa funcao calcular quantas vezes num tem que ser dividido
    #para chegar em 1, o que é o log²(num)=[]
    piso = num
    cont = 0
    while piso != 1:
        piso = piso // 2
        cont+=1
    return cont
#Passo 0.2 Iniciar variaveis

#Passo 1. Ler entrada
num = int(input())
#Passo 2. Encontrar log²(num)
resposta = piso_log(num)
#Passo 3. Imprimir resposta
print(resposta)