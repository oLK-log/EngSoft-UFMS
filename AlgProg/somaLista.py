# -*- coding: utf-8 -*-
# Programa: exer5
# Programador:Lorran Kaíque
# Data: 16/05/2025
# Este programa deve receber uma lista e somar os valores dela
#entrada: list lista
#saida: float soma
#Passo 0: Inicializar variaveis
soma = 0.0
#Passo 1: Receber lista
lista = list(map(float, input().split()))
#Passo 2: Somar elementos da lista
for i in range(len(lista)):
    soma += lista[i]
#Passo 3: Imprimir
print('{0:.2f}'.format(soma))