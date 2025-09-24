# -*- coding: utf-8 -*-
# Programa: varianciaf.py
# Programador:
# Data: 04/09/2010
# Este programa lê quatro notas de provas, calcula a média, a variância
# e o desvio padrão das quatro provas. O programa usa funções para
# computar a variância e o desvio padrão.
# declaração dos módulos utilizados
import math

# definição das funções
def somamediaprovas(p1, p2, p3, p4):
# Passo mp.1. Calcule a soma das notas das provas
   somaprovas = p1 + p2 + p3 + p4
# Passo mp.2. Calcule a média das provas
   mediaprovas = somaprovas/4.0

   return somaprovas, mediaprovas

def variancia(p1, p2, p3, p4, somaprovas):
# Passo v.1. Calcule a soma dos quadrados das notas
   somaquadrado = p1**2 + p2**2 + p3**2 + p4**2
# Passo v.2. Calcule a variância
   var = somaquadrado/4.0 - (1.0/(4**2))*somaprovas**2	

   return var

def desviopadrao(variancia):
# Passo dp.1. Calcule o desvio padrão
   dpadrao = math.sqrt(variancia)
	
   return dpadrao

# início do módulo principal
# descrição das variáveis utilizadas
# float prova1, prova2, prova3, prova4
# float somap, mediap, varia, desviop

# pré: prova1 prova2 prova3 prova4

# Passo 1. Leia as notas das provas.
prova1, prova2, prova3, prova4 = map(float, input().split())
# Passo 2. Calcule a média das provas, variância e desvio padrão
# Passo 2.1. Calcule a soma e a média das provas
somap, mediap = somamediaprovas(prova1, prova2, prova3, prova4)
# Passo 2.2. Calcule a variância das provas
varia = variancia(prova1, prova2, prova3, prova4, somap)
# Passo 2.3. Calcule o desvio padrão
desviop = desviopadrao(varia)
# Passo 3. Imprima os resultados
print('Primeira Prova    {0:4.1f}'.format(prova1))
print('Segunda Prova     {0:4.1f}'.format(prova2))
print('Terceira Prova    {0:4.1f}'.format(prova3))
print('Quarta Prova      {0:4.1f}'.format(prova4))

print('Média das Provas {0:6.2f}'.format(mediap))
print('Variância        {0:6.2f}'.format(varia))
print('Desvio Padrão    {0:6.2f}'.format(desviop))

# pós: media == Soma i em {0,1,2,3}: prova[i] and variancia ==
#      ((1/n)(Soma i em {0,1,2,3}: (prova[i])**2) -
#      (1/n**2)(Soma i em {0,1,2,3}: prova[i])**2)) and
#      desviopadrao == math.sqrt(variancia)
# fim do módulo principal