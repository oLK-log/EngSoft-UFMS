# -*- coding: utf-8 -*-
# Programa: perimetroAreaDef.py
# Programador: Lorran Kaique
# Data: 06/07/2025
# Este programa a partir de um valor de raio de um circulo
#imprime o raio, perimetro e area
import math
#Passo 0. Inicializar asbstracoes
#Passo 0.1 Inicializar funcoes
def perimetroAreaC(raio):
    perimetro = 2* math.pi * raio
    area = math.pi * (raio**2)
    return perimetro, area
def imprimirResultado(perimetro,area):
    print('Raio      = {:6.2f}'.format(raio))
    print('Perimetro = {:6.2f}'.format(y))
    print('Area      = {:6.2f}'.format(z))
#Passo 1.Ler entrada
raio = float(input())
#Passo 2. Encontrar perimetro(y) e area(z)
y,z = perimetroAreaC(raio)
#Passo 3. Imprimir resultados
imprimirResultado(y,z)
