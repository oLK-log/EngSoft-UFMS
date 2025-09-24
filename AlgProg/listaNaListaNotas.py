# -*- coding: utf-8 -*-
# Programa: notas01l.py
# Programador:lorran kaique
# Data: 21/05/25
# Este programa lê um registro com o nome (primeiro nome e
# sobrenome, as 3 notas das provas e as 2 notas de trabalho da
# disciplina de Algoritmos e Programação I. A média das provas é
# dada por MP = (P1+P2+P3)/3.0, a média dos trabalhos por
# MT = (T1 + T2)/2.0 e a média final por MF = 0.75*MP + 0.25*MT.
# O programa computa a média final e imprime o nome, e a média
# final de cada aluno usando um formato específico.
# descrição das variáveis utilizadas
maxfatorPO# list  rga, nome, notas, mf
# float mp, mt
# int   tam
#Passo0: Iniciar variaveis
conjuntoDados = []
somaP = 0
somaT = 0
#Passo 1: Ler
comp = int(input())
for i in range (comp):
    conjuntoDados.append(list(map(str, input().split(','))))
#Passo 2: Criar novo conjunto de lista
novoConj = conjuntoDados.copy()
for i in range(comp):
    notas_str = conjuntoDados[i][2].strip().split(' ')
    notas_float = [float(nota) for nota in notas_str]
    for p in range(0, len(notas_float)):
        if p <3:
            somaP += notas_float[p]
        else:
            somaT += notas_float[p]
    media = (somaP/3)*0.75 + (somaT/2)*0.25
    novoConj[i][2] = media
    media = 0
    somaP = 0
    somaT = 0
#Passo 3: Imprimir novoConjunto
# Passo 3: Imprimir novoConjunto no formato específico
# Itera sobre cada estudante (que é uma lista) em 'novoConj'
for estudante in novoConj:
    rga_aluno = estudante[0]
    nome_aluno = estudante[1]
    mf = estudante[2]
    print(f"{rga_aluno:<6} {nome_aluno:<25} {mf:6.1f}")
# pré: tam para i em {0..tam-1}: rga[i], nome[i], notas[0] notas[1]
#      notas[2] notas[3] notas[4]}


# pós: para i em {1,..,tam}:pnome snome notas mf and  
#      mf ==  0.75*mp + 0.25*mf and 
#      mp == (notas[0] + notas[1] + notas[2])/3.0 and
#      mt == (notas[3] + notas[4])/2.0
# fim do módulo principal
