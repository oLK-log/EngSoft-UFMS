# -*- coding: utf-8 -*-
# Programa: TasteList.py
# Programador: Lorran Kaíque
# Data: 05/07/25
# Este programa a partir de uma lista de fruta e sua nota(com, ruim, medio)
#mostra os sucos mais vendido
#os mais apreciados
#os menos apreciados
#pensamento: a cada sabor adicionado é precisado verificar se ele ja existe, se
#existir, adicionar 1 a venda dele, se não adicionar a tabela
#Passo 0. Inicializar variaveis e abstracoes
key1 = ['name','qtSold','good','average','poor']
key2= ['name','qtd']
entry = []
tasteList = []
goodList=[]
maxList = []
poorList = []
#Passo 1. Ler quantidade de entradas
tam = int(input())
#Passo 2. Ler dados dos sabores
for i in range(tam):
    entry = input().split()
#Passo 3. Verificar se ja existe na nossa lista
    for productDict in tasteList:
        if entry[0] == productDict['name']:
            productDict['qtSold'] += 1
            break
    else:
        products = {
                'name' : entry[0],
                'qtSold' : 1,
                'good' : 0,
                'average' : 0,
                'poor' : 0
                }
        tasteList.append(products)
#Passo 4. acrescentar quantidade a nota
    for productDict in tasteList:
        if entry[0] == productDict['name']:
            if entry[1] == "bom":
                productDict['good'] += 1
            elif entry[1] == "medio":
                productDict['average'] += 1
            else:
                productDict['poor'] += 1
#Passo 5. Encontrar suco mais vendido
#Passo 5.1 Criar variaveis auxiliares
maior = 0
nameMaior =''
good = 0
nameGood = ''
poor = 0
namePoor = ''
#Passo 5.2 Achar o maior valor
for productDict in tasteList:
    if productDict['qtSold'] > maior:
        maior = productDict['qtSold']
#Passo 5.3 Verificar se existem valores iguais
for productDict in tasteList:
    if productDict['qtSold'] == maior:
        entry = {
            'name' : productDict['name'],
            'qtd' : maior
            }
        maxList.append(entry)        
#Passo 6. Achar o que teve a maior qtd de good
for productDict in tasteList:
    if productDict['good'] > good:
        good = productDict['good']
#Passo 6.1 Verificar se existem valores iguais
for productDict in tasteList:
    if productDict['good'] == good:
        entry = {
            'name' : productDict['name'],
            'qtd' : good
            }
        goodList.append(entry) 
#Passo 7. Achar o que teve a maior qts nota poor
for productDict in tasteList:
    if productDict['poor'] > poor:
        poor = productDict['poor']
#Passo 7.1 Verificar se existem valores iguais
for productDict in tasteList:
    if productDict['poor'] == poor:
        entry = {
            'name' : productDict['name'],
            'qtd' : poor
            }
        poorList.append(entry)
#Imprimir resultados
#Imprimir os maisvendidos
for maisVendido in maxList:
    print(

























#tam2 = len(tasteList)
#    if tam2 > 0:
#        presence= False
#        for x in range(tam2):
#            if entry[0] == tasteList[x]['name']:
#            tasteList[x]['qtSold'] += 1
#            presence = True
#Passo 3.1 Se não existir, adicionar
#        if presence == False:
#            products = {
#                'name' : entry[0]
#                'qtSold' : 1
#                'good' : 0
#                'average' : 0
#                'poor' : 0
#                }
#            tasteList.append(products)
            

    #for name in taste
    
