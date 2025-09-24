# -*- coding: utf-8 -*-
# Programa: campanhiaTelefonica.py
# Programador: Lorran Kaíque
# Data: 03/07/25
#Esse programa lê um numero n de assinantes, dados dos n assinantes que serao
#armazenados em uma lista de dicionários composto por 3 strings
#a primeira armazena o sobrenome do assinante
# a segunda o nome
# a terceira o numero do telefone
#não existem 2 clientes com o mesmo nome e sobrenome
#por fim, o programa mostra o nome e telefone dos consultados
#INICIO
#descricao variaveis
#dict contato{}, consulta{}
#list listaContatos, listaConsulta
#int tam, qt
#str numero, nomeC, sobrenomeC, telefoneC
#boolean encontrado

#PAsso 0. Inicializar as variaveis
chaves = ['nome','sobrenome', 'telefone']
listaContatos = []
listaConsulta = []
numero = "não tem telefone"#variavel para pegar o numero do consultado
#contatos = dict.fromkeys(chaves)
#Passo 1. Ler a entrada
#Passo 1.1 ler numero de contatos
tam = int(input())
#PAsso 1.2 ler contatos
for i in range(tam):
    sobrenomeC, nomeC, telefoneC = input().split(",")
    nomeC = nomeC.strip()
    telefoneC = telefoneC.strip()
    contato = {
        'nome': nomeC,
        'sobrenome': sobrenomeC,
        'telefone': telefoneC
        }
    listaContatos.append(contato)
#PAsso 2 Ler a consulta
#Passo 2.1 ler a quant de consultas a serem feitas
qt = int(input())
#Passo 2.2 ler o que será consultado
for i in range(qt):
    nomeC, sobrenomeC= input().split()
    consulta = {
        'nome': nomeC,
        'sobrenome': sobrenomeC
        }
    listaConsulta.append(consulta)
#Passo 3. Procurar na listaContatos os valores da listaConsulta
for i in range(qt):
    encontrado = False
    for x in range(tam):
        if listaContatos[x]['nome'] == listaConsulta[i]['nome'] and listaContatos[x]['sobrenome'] == listaConsulta[i]['sobrenome']:
            print(listaContatos[x]['nome'] + " " + listaContatos[x]['sobrenome'] +" "+ listaContatos[x]['telefone'])
            encontrado = True
            break
    if encontrado == False:
           print(listaConsulta[i]['nome'] + " " + listaConsulta[i]['sobrenome'] +" "+ numero)