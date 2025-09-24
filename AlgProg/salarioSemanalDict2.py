# -*- coding: utf-8 -*-
# Programa: salarioSemanalDict2.py
# Programador: Lorran Kaíque
# Data: 05/07/25
# Este programa lê um conjunto de registros com o número, nome,
# setor, data de ingresso, horas trabalhadas na semana e valor do
# salário por hora e calcula o salário semanal de cada funcionário.
# O programa imprime o número, nome e salário de cada funcionário
#Descricao das variaveis
#list cadastro, folha, chave1, chave2
#int tam

#Passo 1. Ler a entrada e inicializar as variaveis
#Passo 1.1 Ler o numero de funcionarios
tam = int(input())
#Passo 1.2 Inicializar as abstracoes
chave1 = ['num','nome','setor','data','horas','salarioh']
cadastro = [dict.fromkeys(chave1) for _ in range(tam)]
chave2 = ['num','nome','salario']
folha = [dict.fromkeys(chave2) for _ in range(tam)]
dado = [] #ler as entradas
#Passo 1.3 Ler o cadastro da empresa
for i in range(tam):
#Passo 1.3.1 Ler os dados dos funcionarios
    dado = input().split(',')
    cadastro[i]['num'] = dado[0]
    cadastro[i]['nome'] = dado[1]
    cadastro[i]['setor'] = dado[2]
    cadastro[i]['data'] = dado[3]
    cadastro[i]['horas'] = int(dado[4])
    cadastro[i]['salarioh'] = float(dado[5])
#Passo 2. Calcular os salarios
#Passo 2.1 calcular os salarios do funcionario i
for i in range(tam):
    horasExtra = 0.5*(cadastro[i]['horas']-40)*cadastro[i]['salarioh']
    valor = (cadastro[i]['horas']*cadastro[i]['salarioh'])+horasExtra
#Passo 2.1.1 Copia parte da lista de dicionario
    folha[i]['num'] = cadastro[i]['num']
    folha[i]['nome'] = cadastro[i]['nome']
#Passo 2.1.2 Atualiza um campo na lista de dicionario
    folha[i]['salario'] = valor
#Passo 3. Imprime os resultados
for i in range(tam):
    print('{0:s} '.format(folha[i]['num']),end='')
    print('{0:s} {1:.2f}'.format(folha[i]['nome'], folha[i]['salario']))