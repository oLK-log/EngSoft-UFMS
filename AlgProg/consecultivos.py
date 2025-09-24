# -*- coding: utf-8 -*-
# Programa: consecutivos.py
# Programador: lorran kaíque Silveira Fernandes
# Data: 28/04/2025
# Este programa lê um número inteiro e computa se o número contém
# dígitos consecutivos iguais.
# início do módulo principal
# descrição das variáveis utilizadas
# int numero, temp, num
# str msg

# pré: numero

# Passo 1. Leia um número e inicialize as variáveis
# Passo 1.1. Leia um numero
numero = int(input())
# Passo 1.2. Incialize as variaveis msg e temp
log = False
msg = ''
anterior = 0
# Passo 2. Decomponha o numero 
while numero > 0:
    if anterior == (numero%10):
        log = True
    anterior = (numero%10)
    numero = numero // 10
if log == True:
    msg = 'sim'
else:
    msg = 'não'
# Passo 2.1. Calcule o digito menos significativo

# Passo 2.2. Verifique se e igual a digito anterior


 # finaliza a verificacao
  # fim if
# Passo 2.3. Armazene o digito em temp
  
# Passo 2.4. Retire o digito menos significativo
  
# fim while
# Passo 3. Imprime o resultado
print('{0:s}'.format(msg))

# pós: 'sim' and num or 'não'
# fim do módulo principal
