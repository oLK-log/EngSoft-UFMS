# -*- coding: utf-8 -*-
# Programa: salarioSemanalDict.py
# Programador: Lorran Kaíque
# Data: 04/07/25
#Esse programa deseja, dado listas de funcionario, saber o salario semanal de cada um
#Os dados fornecidos são numeroFuncionario, nome, setor, dataIngresso, horasTrab, valorHora
#O funcionario tem um jornada de 40h/s e o que passa disso tem 50% adicional
#Vaviaveis
#int tam
#float pay, time
#list entrada[{}], chave1, chave2
#dict dados, pagamento
#Passo 0. inicializar variaveis
#Passo 0.1 Ler qtd de variaveis
tam = int(input())
#Passo 0.2 Iniciar variaveis
chave1 = ['num','name','sector','date','hr','salary']
chave2 = ['num','name','salary']
employee = [dict.fromkeys(chave1) for _ in range(tam)]
pag = [dict.fromkeys(chave2) for _ in range(tam)]
entry = []
#Passo 1. Ler dados
for i in range(tam):
    entry = input().split(',')
    entry = [item.strip() for item in entry] #limpas os espaços
    
    employee[i]['num'] = int(entry[0])
    employee[i]['name'] = entry[1]
    employee[i]['sector'] = entry[2]
    employee[i]['date'] = entry[3]
    employee[i]['hr'] = float(entry[4])
    employee[i]['salary'] = float(entry[5])
#Passo 2.Gerar novo dicionario com os salarios
#PAsso 2.1 Calcular salario
for i in range(tam):
    entry = []
    entry.append(employee[i]['num'])
    entry.append(employee[i]['name'])
    time = employee[i]['hr']
    if time > 40:
        pay = 40*employee[i]['salary'] + ((time - 40)*1.5)*employee[i]['salary']
    else:
        pay = time*employee[i]['salary']
    entry.append(pay)
    pag[i]['num'] = entry[0]
    pag[i]['name'] = entry[1]
    pag[i]['salary'] = entry[2]
#Passo 3. Imprimir novas listas
    print(f"{pag[i]['num']:05d} {pag[i]['name']} {pag[i]['salary']:.2f}")
