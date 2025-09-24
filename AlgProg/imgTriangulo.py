# -*- coding: utf-8 -*-  
# Programa: triangulopil.py
# Programador:
# Data: 27/08/2020
# Este programa utiliza os módulos math e PIL (pillow).
# Ele gera e imprime um triângulo.
# Declaração dos módulos utilizados
import math
from PIL import Image, ImageDraw  
# início do módulo principal
# descrição das variáveis utilizadas  
# Image tela
# ImageDraw desenhe
# int largura, altura
# str padrao
# pré: void
# Passo 1. Defina o ambiente gráfico
# Passo 1.1. Defina o tamanho da tela 
largura = 900
altura = 600 
# Passo 1.2. Defina o padrão de cores
padrao = 'RGB'  
# Passo 1.3. Crie a tela
tela= Image.new(padrao, (largura,altura),color='white')
desenhe = ImageDraw.Draw(tela)
# Passo 2. Gere um triângulo equilátero de 300 pixels de lado
# Passo 2.1. Desenhe uma linha (base do triângulo)
desenhe.line((300, 500, 600, 500),fill=(255, 0, 0), width=1)
# Passo 2.2. Compute a altura do triângulo
altura = (math.sqrt(3.0)/2.0)*300
# Passo 2.3. Desenhe uma linha (lado)
desenhe.line((300, 500, 450, altura),fill=(255, 0, 0), width=1)
# Passo 2.4. Desenhe uma linha (lado)
desenhe.line((450, altura, 600, 500),fill=(255, 0, 0), width=1)  
# Passo 3. # Passo 3. Imprima o triângulo
tela.show()
# pós: um triângulo
# fim do módulo principal