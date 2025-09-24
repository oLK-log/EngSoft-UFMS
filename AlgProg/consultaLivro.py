# -*- coding: utf-8 -*-
# Programa: consultaLivro.py
# Programador: Lorran Kaíque
# Data: 08/06/25
# Este programa, dada uma lista de livros n[nome, estante]
# e outra com m [nomes],  quer o nome do autor e a prateleira de cada um dos livros
#caso não exista correespondencia- "não encontrado"
#entrada: arquivo biblioteca.in = [n(numero livros)][m(nomeLivro, nomeAutor, estante)].
#m=[numero de livros dados]
#Passo 0. Iniciar variaveis
acervo = []
consulta = []
v = 0
#Passo 1. Ler os dados
#Passo 1.1 Ler base de dados biblioteca
n = int(input())
for i in range(n):
    ent = input().split(",")
    semEsp = [item.strip() for item in ent]
    acervo.append(semEsp)
#Passo 1.2 Ler informação de consulta
c = int(input())
for i in range(c):
    consulta.append(input())
#Passo 2. Ver se livros de consulta tem correespondencia em acervo
for i in range(0, c):
    for j in range(0, n):
        if consulta[i] == acervo[j][0]:
            print("{0} {1}".format(acervo[j][1], acervo[j][2]))
            v = 1
    if v == 0:
        print("{0} não encontrado".format(consulta[i]))
    v = 0