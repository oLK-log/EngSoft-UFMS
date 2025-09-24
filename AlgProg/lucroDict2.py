# -*- coding: utf-8 -*-
# Programa: lucroDict2.py
# Programador: Lorran Kaíque
# Data: 04/07/25
#Este algoritmo lÊ um conjunto de registros com o numero, nome
#estoque, preco de custo e preco de venda e calcula o provavel
# lucro total se cada item for vendido
#Inicio
#variaveis
#list estoque[{}], receita[{}], chaves1, chaves2
#dict produto, fatura
#int tam

#Passo 1. Ler a entrada e inicializar as variaveis
#PAsso 1.1 Ler o tamanho do estoque
tam = int(input())
#Passo 1.2 Inicialize as abstracoes
chave1 = ['num','nome','qtde','custo','venda'] #chaves do dicionário
chave2 = ['num','nome','lucro']#chaves do dicionário
estoque = [dict.fromkeys(chave1) for _ in range(tam)] #lista de dicionarios de produto
receita = [dict.fromkeys(chave2) for _ in range(tam)] #lista de dicionários de fatura
produto = [] #lista para ler a entrada
#Passo 1.3 Leia o estoque
for i in range(tam):
#Passo 1.3.1 Leia o produto
    produto = input().split() #lido como uma lista de str
    estoque[i]['num'] = produto[0]
    estoque[i]['nome'] = produto[1]
    estoque[i]['qtde'] = int(produto[2])#ja converte para int
    estoque[i]['custo'] = float(produto[3])#ja converte para float
    estoque[i]['venda'] = float(produto[4])#ja converte para float
#Passo 2. Calcular o provavel lucro
#Passo 2.1 calcular o lucro de cada item
for i in range(tam):
    valor = (estoque[i]['venda']-estoque[i]['custo'])*estoque[i]['qtde']
#Passo 2.1.1 Copiar parte do dicionario
    receita[i]['num'] = estoque[i]['num']
    receita[i]['nome'] = estoque[i]['nome']
#Passo 2.1.2 Adiciona um campo ao dicionario
    receita[i]['lucro'] = valor
#Passo 2.2 Lucro total
total = sum(receita[i]['lucro'] for i in range(tam))
#Passo 3. Imprimir os resultados
print('{0:.2f}'.format(total))