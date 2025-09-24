# -*- coding: utf-8 -*-
# Programa: jornadaPart
# Programador: Lorran Kaíque
#Este programa deseja para cada posicao da particula, determinar qual filtro ira parar ela
#Passo 0. Inicializar variaveis
vetor = []
x= 0
#Passo 1> entrada
#Passo 1.1 ler N-numero de filtros K - numero de aumento
n, k = map(int, input().split())
#Passo 1.2 ler lista
lista = list(map(int, input().split()))
#Passo 2. logica
for i in range(0, n):
    filtroAtual = i
    momento = lista[i]

    while x == 0:
        limite = lista[i]
        if momento > limite:
            vetor.append(filtroAtual)
            x = 1
        else:
            momento += k
            filtroAtual = (filtroAtual % n) + 1
    x = 0
print(*vetor)
            