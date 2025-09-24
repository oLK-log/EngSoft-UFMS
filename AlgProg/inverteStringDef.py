# Programa: inverteStringDef.py
# Programador: Lorran Kaique
# Data: 08/07/2025
# Este programa informa se uma palavra fornecida é palindromo ou não
#pre: str
#pos: resposta
#Passo 0.Definir abstracoes
#Passo 0.1 criar funcoes
def inverte(palavra):
    #inverte uma palavra
    #ler uma palavra e falar se é políndromo
    #entra:str palavra
    inversa = ""
    for letra in palavra:
         inversa = letra +inversa

    if palavra != inversa:
        print("não é palíndromo")
    else:
        print("palíndromo")
#Passo 1. Ler entrada
palavra = input()
#Passo 2. rodar a funcao
inverte(palavra)
