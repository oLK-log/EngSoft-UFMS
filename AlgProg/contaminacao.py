# -*- coding: utf-8 -*-
# Programa: contaminacao00.py
# Programador:lk
# Data: 13/04/25
# Este programa simula um modelo simplificado de contaminação. O
# programa lê dois números inteiros representando o número incial
# de pessoas contaminadas com um determinado vírus e o um dado
# período de tempo. Cada pessoa contaminada contamina 4 novas
# pessoas por dia. Compute o total de pessoas contaminadas ao final
# de um dado período.
# início do módulo principal
# descrição das variáveis utilizadas
# int contIni, dias
# int contFinal
contInicial = int(input("Digite o número de pessoas contaminadas:\n"))
dias = int(input("Digite o número de dias de contaminação:\n"))
contFinal = 0
# pré: containi dias
while dias != 0:
    dias -= 1
    contFinal = contInicial*4
#no final de um dia, o número de contaminados é os novos + os antigos
    contInicial += contFinal
print(contInicial)
# pós: contafinal
# fim do módulo principal
