# -*- coding: utf-8 -*-
#Questao 1 lista
# Programa: areaperimetroT.py
# Programador: Lorran Kaíque Silveira Fernandes
# Data: 26/04/2025
# Diálogo: Este lê o valor dos lados de um triângulo e calcula o 
# perímetro e a área do triângulo e imprime o resultado.
# decalaração dos módulos utilizados
#ler 3 valores reais que representa os lados do triângulo
#calcular perímetro
#calcular área
#fórmula de heron: a=raiz s(s-l1)(s-l2)(s-l3)
#entrada:
#float. l1, l2, l3;
#saida
#float(5casas). perimetro, area
#importanto biblioteca math
import math
#Passo 1: ler os lados do triangulo
l1= float(input())
l2= float(input())
l3= float(input())
#Passo 2:calcular o perímetro e o semiperimetro
perimetro = l1 + l2 + l3
s= perimetro / 2
#Passo 3: Calcular a área do triângulo
area = (s*(s-l1)*(s-l2)*(s-l3))**(1/2)
#Passo 4: Imprimir o lado, perímetro e área
print('Lados = {0:5.2f}, {1:5.2f}, {2:5.2f}'.format(l1, l2, l3))
print('Perímetro = {0:5.2f}'.format(perimetro))
print('Área = {0:5.2f}'.format(area))