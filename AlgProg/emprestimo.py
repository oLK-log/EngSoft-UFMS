# -*- coding: utf-8 -*-
# Programa: fibonaci02.py
# Programador: lORRAN kAÍQUE
# Data: 05/05/2025
# Este programa lê o valor de empréstimo, taxa de juros e pagamento mensal
#entradas: float vEmpr, tx, pg
#saída: int nPag, float pg, juros, saldoDev
#Passo1: Ler valores
vEmpr = float(input())
tx = float(input())
pg = float(input())
#Passo 2 Imprimir cabeçalho:
print("Pagamento No.  Pagamento    Juros  Saldo Devedor\n================================================")
#Passo 3: Variaveis
#O juros é mensal é R/12 %
#Passo 3.1: Calcular o jurosMensal
jurosMensal = (tx/12)/100
#Passo 3.2: Inicie as variaveis
nPag = 1
juros = 0.0
saldoDev = vEmpr
totalJuros = 0
#Passo 4: Calculo e impressão
while saldoDev != 0:
    if saldoDev >= pg:
        juros = jurosMensal * saldoDev
        totalJuros += juros
        saldoDev = saldoDev - pg + juros
        print('{0:5d}{1:19.2f}{2:10.2f}{3:14.2f}'.format(nPag, pg, juros, saldoDev))
        nPag +=1
    else:
        juros = jurosMensal * saldoDev
        totalJuros += juros
        pg = saldoDev + juros
        saldoDev = 0.00
        print('{0:5d}{1:19.2f}{2:10.2f}{3:14.2f}'.format(nPag, pg, juros, saldoDev))
print('\n\nTotal de Juros = {0:12.2f}'.format(totalJuros))