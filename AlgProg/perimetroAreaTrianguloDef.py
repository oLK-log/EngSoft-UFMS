# -*- coding: utf-8 -*-
# Programa: perimetroAreaTrianguloDef.py
# Programador: Lorran Kaique
# Data: 06/07/2025
# Este programa le o valor dos lados de um triangulo e
#imprime OS LADOS, o perimetro e area
#Importacoes
import math
#Passo 0. Inicializar abstracoes
#Passo 0.1. inicializar funcoes
#funcao de descobrir perimetro e area de um triangulo
def perimetroAreaT(lado1, lado2, lado3):
    perimetro = lado1+lado2+lado3
    semip = perimetro/2.0
    
    area = math.sqrt(semip*(semip-lado1)*(semip-lado2)*(semip-lado3))
    return perimetro, area
#funcao para imprimir os resultados(lados, perimetro e area)
def imprimir(lado1,lado2,lado3,perimetro,area):
    print('Lados = {0:5.2f}, {1:5.2f}, {2:5.2f}'.format(lado1, lado2, lado3))
    print('Perímetro = {0:5.2f}'.format(perimetro))
    print('Área = {0:5.2f}'.format(area))
#Passo 1. Ler os valores dos lados
lado1,lado2,lado3 = map(float, input().split())
#passo 2. Encontrar o perimetro e area
perimetro, area = perimetroAreaT(lado1,lado2,lado3)
#Passo 3. Imprimir valores
imprimir(lado1,lado2,lado3,perimetro,area)