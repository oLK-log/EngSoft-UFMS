# -*- coding: utf-8 -*-
# Programa: DicionarioDiaSeguinte.py
# Programador: Lorran Kaíque
# Data: 09/07/2025
# Este programa le uma data e imprime a data do dia seguinte

# Passo 0.2 criar funcoes
def bissexto(ano):
    #Verifica se um ano é bissexto.
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False

# Passo 1. Ler entradas
dia, mes, ano = map(int, input().split('/'))

# Passo 1.2 Armazenar em um dicionario
data_hoje = {
    'dia' : dia,
    'mes' : mes,
    'ano' : ano
}

# Passo 2. Encontrar dia seguinte:
dias_no_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#se for ano bissexto, Fevereiro tem 29 dias
if bissexto(data_hoje['ano']):
    dias_no_mes[2] = 29

#Passo 2.1 Inicializa a data de amanhã com os valores de hoje
dia_seguinte = data_hoje['dia']
mes_seguinte = data_hoje['mes']
ano_seguinte = data_hoje['ano']

#Passo 2.2 Verifica se o dia de hoje é o último dia do mês
if data_hoje['dia'] == dias_no_mes[data_hoje['mes']]:
    # Se for, o dia seguinte é 1
    dia_seguinte = 1
    # E o mês avança
    mes_seguinte += 1
    # Verifica se houve virada de ano
    if mes_seguinte > 12:
        # Se sim, o mês vira 1 e o ano avança
        mes_seguinte = 1
        ano_seguinte += 1
else:
    # Se não for o último dia do mês, apenas o dia avança
    dia_seguinte += 1

#PAsso2.3  Cria o dicionário para a data do dia seguinte
data_amanha = {
    'dia': dia_seguinte,
    'mes': mes_seguinte,
    'ano': ano_seguinte
}

# Passo 3. Imprimir a data do dia
print(f"{data_amanha['dia']:02d}/{data_amanha['mes']:02d}/{data_amanha['ano']:04d}")