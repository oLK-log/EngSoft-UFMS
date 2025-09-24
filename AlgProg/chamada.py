import math
#1.55 por minuto
#valores decimais de minutos são aproximados ao prox valor inteiro
#o valor é acres + 0.28 de imposto
#ligações p msm op n são tarifadas
valorCred = float(input("Quantos créditos você possui?\n"))
dur = float(input("Quanto tempo durou a chamada?\n"))
dur = int(math.ceil(dur))
valorChamada = dur*1.55
valorImposto = valorChamada*0.285
valorTotal = valorChamada*1.285
saldo = valorCred - valorTotal
print('Valor dos Créditos :R$ {0:7.2f}'.format(valorCred))
print('Valor da Chamada :R$ {0:7.2f}'.format(valorChamada))
print('Valor dos Impostos :R$ {0:7.2f}'.format(valorImposto))
print('Valor Total da Chamada :R$ {0:7.2f}'.format(valorTotal))
print('Valor do Saldo Atual :R$ {0:7.2f}'.format(saldo))