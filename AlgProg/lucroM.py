# -*- coding: utf-8 -*-
# Programa: publicidade.py
# Programador:
# Data: 21/01/2013
# Este algoritmo lê o número de armários vendidos por mês,
# o lucro por armário e os custos de publicidade e operacional da empresa.
# Calcula quanto deve ser investido em publicidade até que o lucro da empresa
# comece a diminuir.

# pré: numArmarios lucroArmario custoPublicidade custoOperacional
#Receita = 

# Passo 1. Leia os dados de entrada
# Passo 1.1. Leia o número de armário vendidos
#strip remove espaço extra (final e inicio)
lista = input().strip()
numArm, lucroArm, custoPub, custoOp = lista.split(' ')
numArm = int(numArm)
# Passo 1.2. Leia o lucro por armário
lucroArm = float(lucroArm)
# Passo 1.3. Leia o custo de publicidade
custoPub = float(custoPub)
# Passo 1.4. Leia o custo operacional
custoOp = float(custoOp)
n = 0.0
x = 0.0
lucroA = (numArm * lucroArm) - custoPub - custoOp
numArmA = numArm
custoPubA = custoPub
#while x != 1:
#    receita = (int(numArm*(1.2**n))) * lucroArm
#    lucro = receita - (custoPub*(2**n)) - custoOp
#    if lucro < lucroA:
#        x = 1
#    n+=1
#    lucroA = lucro
#numArm = int(numArm*(1.2**(n-1)))
#custoPub = custoPub*(2**(n-1))
while True:
    numArm = int(numArm * 1.2)
    custoPub *= 2
    lucro = (numArm * lucroArm) - custoPub - custoOp
    if lucro <= lucroA:
        break
    else:    
        lucroA = lucro
        numArmA = numArm
        custoPubA = custoPub
# Passo 2.3. Compute o investimento máximo em publicidade

# Passo 2.3.1. Atualize o número de vendas e o custo de publicidade

# Passo 2.3.2 Calcule o novo lucro com o aumento da publicidade

# Passo 5. Imprima os resultados
print('{0:3d} {1:10.2f} {2:10.2f}'.format(numArmA, custoPubA, lucroA))

# pós: numArmarios, custoPublicidade, lucro
