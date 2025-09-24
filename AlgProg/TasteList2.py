# -*- coding: utf-8 -*-
# Programa: TasteList2.py
# Programador: Lorran Kaíque
# Data: 06/07/25
# Este programa gera aleatoriamente uma amostra de sucos e a
#avaliacao dos consumidores relativa aps sucos consumidos
#O programa computa o numero de sucos comercializados e quais sucos foram mais apreciados e quais foram menos
#biblioteca utilizada
import random
#variaveis
# list sucos[{}], chaves, tipos, amostra ,avalia
# list lvendas, lavabom, lavaruim
#list lmais, lbom, lruim
#int maxvendas, maxbom, maxruim

#Passo 1. Definindo estrutura e inicializando variaveis
#Passo 1.1 Definindo s lista das chaves
chaves = ['nome','vendas','avalia']
#Passo 1.2 Inicializar a lista dos tipos de suco
tipos = ['araticum','butia','cagaita','caja','guavira','inga','jabuticaba','jaracatia','mangaba']
#Passo 1.3 inicializar a lista de sucos
sucos = [dict.fromkeys(chaves) for _ in range(len(tipos))]
#Passo 1.4 guarde o dicionario na lista
for i in range(len(tipos)):
    sucos[i]['nome'] = tipos[i]
    sucos[i]['vendas'] = 0
    sucos[i]['avalia'] = [0,0,0]
#Passo 1.5 Gere uma entrada(amostra) aleatoria
random.seed()
avalia = ['bom','medio','ruim']
amostra = [[random.choice(tipos), random.choice(avalia)] for i in range(1000)]
#Passo 2. Compute a quantidade de sucos vendidos e a avaliacao
#Passo 2.1 compute a tabela de vendas
for i in range(len(amostra)): #tamanho da entrada
    for j in range(len(tipos)): #tipos de sucos
        if amostra[i][0] == sucos[j]['nome']:
            sucos[j]['vendas'] += 1
            if amostra[i][1] == "bom":
                sucos[j]['avalia'][0] += 1
            if amostra[i][1] == "medio":
                sucos[j]['avalia'][1] += 1
            if amostra[i][1] == "ruim":
                sucos[j]['avalia'][2] += 1
#Passo 2.2 computar a quantidade dos sucos mais vendidos
maxvendas = max(sucos[i]['vendas'] for i in range(len(tipos)))
#Passo 2.3 computar a quantidade de sucos mais bem avaliados
maxbom = max(sucos[i]['avalia'][0] for i in range(len(tipos)))
#Passo 2.4 computar a quantidade de sucos mais mau avaliados
maxruim = max(sucos[i]['avalia'][2] for i in range(len(tipos)))
#Passo 2.5 computar a lista dos sucos mais vendidos
lmais = [d['nome'] for d in sucos if d['vendas'] == maxvendas]
#Passo 2.6 computar a lista dos sucos mais bem avaliados
lbom= [d['nome'] for d in sucos if d['avalia'][0] == maxbom]
#Passo 2.7 computar a lista dos sucos mais mal avaliados
lruim = [d['nome'] for d in sucos if d['avalia'][2] == maxruim]
#Passo 3. Imprimir os resultados
print('Sucos mais vendidos: ', lmais, maxvendas)
print('Sucos mais apreciados: ', lbom, maxbom)
print('Sucos menos apreciados ', lruim, maxruim)

