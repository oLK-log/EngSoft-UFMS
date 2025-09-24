# -*- coding: utf-8 -*-
# Programa: lucroDict.py
# Programador: Lorran Kaíque
# Data: 04/07/25
#estudo mod 432
#Considere o problema de computar o possível lucro de uma empresa caso todos os seus itens constantes no estoque sejam vendidos. A empresa conta com um sistema de controle de estoque.
#Nesse sistema consta o número, o nome, o estoque atual, o preço de custo e o preço de venda para cada um dos itens da empresa. O gerente da empresa quer saber qual o possível lucro bruto se todos os itens da empresa forem vendidos.
#Projete e implemente um programa que leia o arquivo com o estoque, calcule e imprima o possível lucro bruto de cada item e ao final imprima o possível lucro bruto total da empresa.
## formato de entrada
#12122 transistor 150 1457 9.45 11.23
#11201 capacitor 160 3218 0.90 1.20
#12304 resistor 140 4120 0.10 0.13

# formato de saída
#12122 transistor 2593.46
#11201 capacitor 965.40
#12304 resistor 123.60
#3682.46
#Esse programa le lista de dados de um produto e deseja saber o lucro
#caso todos itens sejam vendidos
#funcao
#def tirarEspacoSepara(entrada):
#    listaComEspaco = entrada.split('')
#    listaLimpa = [item.strip() for item in listaComEspaco]
#    num, produto, qtd, custo, venda = listaLimpa
#    return num, produto, qtd, custo, venda
#variaveis
#list prod, info, lista
#dict produto, lucros
#in tam
#float lucro, lucroTotal
#Passo 0. Inicializar as variáveis
chaves = ['num','nome','qtd','custo','venda','Lucro','Numero','Nome do Produto']
listaProdutos = []
lucroTotal = 0.0
#Passo 1.Receber informações
#Passo 1.1-Receber qunatidades de inf a serem inseridas
tam = int(input())
#Passo 1.2-Receber produtos
for i in range(tam):
    num, produto, qtd, custo, venda = input().split()
    qtd = int(qtd)
    custo = float(custo)
    venda = float(venda)
    produto = {
        'num' : num,
        'nome' : produto,
        'qtd' : qtd,
        'custo' : custo,
        'venda' : venda
        }
    listaProdutos.append(produto)
#Passo 2. Calcular o lucro por produto
for i in range(tam):
    lucro = (listaProdutos[i]['venda']-listaProdutos[i]['custo'])*listaProdutos[i]['qtd']
    lucroTotal+=lucro
#Passo 3. Imprimir resultados
    print(f"{listaProdutos[i]['num']} {listaProdutos[i]['nome']} {lucro:.2f}")
print(f"{lucroTotal:.2f}")