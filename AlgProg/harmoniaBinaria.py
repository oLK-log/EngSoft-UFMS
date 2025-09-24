# -*- coding: utf-8 -*-
# Programa: harmoniaBinaria
# Programador: Lorran Kaíque
#este programa, a partir de uma entrada numeroca,
#quer o maior numero, menor ou igual a entrada, que seja palindromo
#Passo 0: definir funções
#Passo0.1 funcão para ver se é igual ao seu invertido
def sePoli(num):
    bina = bin(num)[2:]
    return bina == bina[::-1]
#Passo 0.2 funcao que encontrar o maior numero
#a partir da entrada, percorre trirando 1
#e usa a funcao para ver se é polindromo
def maior(n):
    for i in range(n, -1, -1):
        if sePoli(i):
            return i
#Passo 1.Ler entrada
n = int(input())
#Passo 2.Imprimir saida ja usando a funcao
print(maior(n))
#ler numero
#nDec = int(input())
#anterior = nDec+1
#Achar o maior <= a nBin que seja palindrom
#como queremos o maior, começar de frente para traz
#v = True
#while v:
#    anterior -= 1
#    antBi = bin(anterior)[2:]
#    reverso = (antBi[::-1])
#    if antBi == reverso:
#       y = antBi
#       v = False
#y = int(y, 2)
#print(y)
#anteriorBi = int(bin(anterior)[2:])