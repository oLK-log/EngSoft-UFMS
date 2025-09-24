# -*- coding: utf-8 -*-
# Programa: contaSucoDicionario.py
# Programador: Lorran Kaíque
# Data: 08/06/25
# Este programa a partir de uma sequencia de sucos vendidos, deseja saber
# qts unidades de cada sabor foi vendida
#Passo 0. Iniciar variaveis
sucoVendido = {}
#Passo 1. Ler o n de entrada
n = int(input())
#Passo 2. Iterar
#Para cada suco lido, verificar se já existe no dicionario.
#Se sim, aumentar o n. Se n, adicionar ao dic
for _ in range(n):
    sabor = input()
    if sabor in sucoVendido:
        sucoVendido[sabor] += 1
    else:
        sucoVendido[sabor] = 1
#Passo 3. Imprimir
for sabor, quantidade in sucoVendido.items():
    print(f"{sabor} {quantidade}")
    
