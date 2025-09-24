# -*- coding: utf-8 -*-
# Programa: medianotas4.py
# Programador:
# Data: 25/11/2016
# Este programa calcula a média final de um aluno para
# um curso com o total de três notas de provas e duas notas de trabalhos.
# A média da disciplina é dada por 0.75 da média das provas somada com
# 0.25 da média dos trabalhos. O alunos pode fazer uma prova optativa
# que substitui a menor nota das provas. Caso a média do aluno seja maior 
# ou igual a 6.0 o aluno e se o aluno tiver frequê3ncia superior a 75%
# o aluno é considerado aprovado ('AP'), caso contrário, o aluno é considerado
# reprovado ('RP'). Se o total de faltas for superior a 25% o aluno é
# considerado reprovado por falta ('RF').
# início do módulo principal
# descrição das variáveis utilizadas
# float prova1, prova2, prova3, trab1, trab2, opt
# float menornota, somaProvas, somaTraba
# flroat mediaProvas, mediaTraba, mediaFinal
# int freq
# str rga, resp

# pré: rga prova1 prova2 prova3 trab1 trab2 freq resp opt

# Passo 1. Leia as notas das provas e trabalhos
# Passo 1.1. Leia a matrícula e as notas
rga = input()
prova1 = float(input())
prova2 = float(input())
prova3 = float(input())
# Passo 1.2. Leia as notas dos trabalhos.
traba1 = float(input())
traba2 = float(input())
# Passo 1.3. Leia a porcentagem da frequência
freq = int(input())
# Passo 1.4. Verifique se o aluno fez a prova optativa
resp = input()
if resp == 'S':
    provaOp = float(input())
else:
    provaOp = 0.0

# Passo 2. Calcule a média da disciplina
# Passo 2.1. Calcule a soma das provas
somaProvas = prova1 + prova2 + prova3
# Passo 2.2. Calcule a soma dos trabalhos
somaTraba = traba1 + traba2
# Passo 2.3. Calcule a Menor Nota
if prova1 < prova2:
    menorNota = prova1
    mN = 1
else:
    menorNota = prova2
    mN = 2
if menorNota > prova3:
    menorNota = prova3
    mN = 3
# Passo 2.4. Troque a menor nota com a prova optativa
if provaOp > menorNota:
    menorNota = provaOp
# Passo 2.5. Calcule a média das provas
if mN == 1:
    soma = prova2 + prova3 + menorNota
elif mN == 2:
    soma = prova1 + prova3 + menorNota
else:
    soma = prova1 + prova2 + menorNota
mediaProva = soma/3
# Passo 2.6. Calcule a média dos trabalhos
mediaTraba =(traba1 + traba2)/2
# Passo 2.7. Calcule a média final da disciplina
mediaFinal = (mediaProva*0.75) + (mediaTraba*0.25)
# Passo 2.8. Faça um arredondamento na média final com uma casa decimal
mediaFinal = round(mediaFinal, 1)
# Passo3. Compute a mensagem correspondente 
if (mediaFinal >= 6) and (freq >= 75):
    msg="AP"
elif (mediaFinal >= 6) and (freq <75):
    msg="RF"
else:
    msg="RN"
# Passo 3. Imprima os resultados
print('{0:s}: Média ={1:5.1f}, Frequência ={2:4d}% - {3:s}'.format(rga,mediaFinal,freq,msg))

# pós: menorNota == min{prova1, prova2, prova3} and
#      ((mediaFinal == 0.75*(prova1+prova2+prova3)/3.0 + 
#      0.25*(trab1+trab2)/2.0) or
#      (mediaFinal == 0.75*(prova1+prova2+prova3-menorNota+opt)/3.0
#      + 0.25*(trab1+trab2)/2.0)) and ((mediaFinal >=6.0 and 
#      freq >= 75 and 'AP') or (mediaFinal < 6.0 
#      and freq >= 75 and 'RN') or (freq < 75 and 'RF'))
# fim do módulo principal
