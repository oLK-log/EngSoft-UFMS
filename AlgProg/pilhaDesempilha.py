# -*- coding: utf-8 -*-
# Programa: pilhaDesempilha.py
# Programador: Lorran Kaique
# Data: 03/06/25
#Estudo:
#Stack-pilha: segue o principio LIFO(Last In, Fist Out)
#Ùltimo a entrar primeiro a sair
# Este programa lê uma quantidade de tarefas, empilha elas, e depois desempilha
#a saída consiste em uma lista de tarefas na ordem que foram desempilhadas
#entrada int n,list tasks
#intermediario list pilha
#saida list desempilha
#pode nome_lista.pop() para desempilhar os elementos
#Passo 0. Iniciar variaveis
desempilha = []
#Passo 1: Ler n e list tasks
n = int(input())
tasks= list(map(int, input().split()))
#Passo 2: Desempilhar
for i in range(0, n):
    desempilha.append(tasks.pop())
#Passo 3: Imprimir
print(desempilha)