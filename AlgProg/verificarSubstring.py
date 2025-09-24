# -*- coding: utf-8 -*-
# Programa: verificarSubstring.py
# Programador: Lorran Kaíque
# Data: 21/01/2013 
# Este algoritmo verifica se uma string de 3 caracteres ocorre em uma frase,
# comparando caracteres individualmente
# entrada: str frase, subFrase
# variaveis: nFrase, nSub
# saída: str resposta

# Passo 0: Inicializar variaveis
nFrase = 0
nSub = 0
resposta = 'não'

# Passo 1: Ler as entradas
frase = input()
subFrase = input()

# Passo 2: Calcular o comprimento
for char in frase:
    nFrase += 1
for char in subFrase:
    nSub += 1

# Passo 3: verificar se contem
# Passo 3.1: Para conter, a frase tem que ser maior ou igual à substring
if nFrase >= nSub:
    for i in range(nFrase - nSub + 1):
        if frase[i] == subFrase[0]:
            if frase[i + 1] == subFrase[1]:
                if frase[i + 2] == subFrase[2]:
                    resposta = 'sim'
                    break

# Passo 4: Imprimir resposta
print(resposta)