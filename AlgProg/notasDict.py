# -*- coding: utf-8 -*-
# Programa: mediaFinalAlunosDic.py
# Programador: Lorran Kaíque
# Data: 08/06/25
#este programa lê o numero, nome, 3 notas de prova e 2 notas de trabalho
# e calcula a media das provas e trabalho usando a fórmula final:
#MF = 0.75*MP + 0.25*MT
#Por fim, ele mostra o numero, nome e media final do aluno
#descricao variaveis:
#list chaves[], dados[]
#dict estudante{}
#float mediaProvas, mediaTrabalhos, mediaFinal
#int tam
#Passo 0. Inicialização das estruturas
chaves = ['numero','nome','notas']
estudante = dict.fromkeys(chaves)
dados = []
#Passo 1. Ler numero de alunos
tam = int(input())
#Passo 2.receber valores
for i in range(tam):
    dados = input().split(',')#lê os dados como uma lista de string
    estudante['numero'] = int(dados[0]) #converte para inteiro
    estudante['nome'] = dados[1]
    estudante['notas'] = list(map(float, dados[2].split())) #lista floats
#Passo 3. Calcular a media final dos alunos
#Passo 3.1 calcular a media provas
    mediaProvas = sum(estudante['notas'][:3])/3.0
#Passo 3.2 calcular a media trabalho
    mediaTrab = sum(estudante['notas'][3:])/2.0
#Passo 3.3 calcular media final
    mediaFinal = 0.75*mediaProvas + 0.25*mediaTrab
#PAsso 4. Imprimir
    print('{0:d} '.format(estudante['numero']), end='')
    print('{0:s} {1:.1f}'.format(estudante['nome'], mediaFinal))





#Declaração das Abstrações
#chave = ['numero','nome','notas']
#estudante = dict.fromkeys(chave) #cria um dicionario vazio

#mediaProvas = (aluno['notas'][0]+aluno['notas'][1]+aluno['notas'][2])/3.0
#mediaTrabalhos = (aluno['notas'][3]+aluno['notas'][4])/2.0

#calcular por meio de funcoes
#soma = sum(aluno['notas'][3])
#mediaProvas = soma/3.0
#soma = sum(aluno['notas'][3])
#mediaTrabalhos = soma/2.0

