# -*- coding: utf-8 -*-
# Programa: produtoDeFracoesDict.py
# Programador: Lorran Kaíque
# Data: 08/06/25
#este programa lê dois numeros racionais no formato p/q
#computa o produto na forma p/q e imprime o resultado
#INICIO
#descricao variaveis
#dict num1{}, num2{}, prod{}
#list num1, num2
#PAsso 0. Inicializar as variaveis
chaves = ['num','den']
num1 = dict.fromkeys(chaves)
num2 = dict.fromkeys(chaves)
#Passo 1. Ler a entrada
#PAsso 1.1 ler a primeira fração
num1['num'],num1['den'] = map(int, input().split('/'))
#Passo 1.2 ler a segunda fração
num2['num'], num2['den'] = map(int, input().split('/'))
#Passo 2 calculas o produto das frações
prod = {i:num1[i]*num2[i] for i in chaves}
#Passo 3. Imprimir os resultados
print('{0:d}/{1:d}'.format(prod['num'], prod['den']))

