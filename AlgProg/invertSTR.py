# -*- coding: utf-8 -*-
# Programa: invertestr.py
# Programador: Lorran Kaíque Silveira Fernandes
# Data: 26/04/2025
# Este programa que lê uma string com quatro caracteres 
# palavra[0:4]. O seu programa deve inverter a ordem dos 
# caracteres de palavra gerar a string
# inversa = palavra[::-1] (sem usar slicing) e imprimir o 
# resultado.
# início do módulo principal
# descrição das variáveis utilizadas
# str palavra, inversa

# Passo 1. Leia a palabra
palavra = input()
# Passo 2. Inverta a palavra
inversa = palavra[3] + palavra [2] + palavra [1] + palavra[0]
# Passo 3. Imprima a palavra invertida
print('{0:s}'.format(inversa))