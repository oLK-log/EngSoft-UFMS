# -*- coding: utf-8 -*-
# Programa: charordem.py
# Programador:lORRAN
# Data: 27/04/2025
# Este programa lê quatro caracteres letra1, letra2, letra3 e letra4 e
# verifica se eles são do alfabeto. Se os caracteres forem do alfabeto,
# o programa verifica se estão em ordem crescente. O programa
# imprime mensagens adequadas.
# início do módulo principal
# descrição das variáveis utilizadas
# str letra1, letra2, letra3, letra4
# str msg

# pré: letra1 letra2 letra3 letra4

# Passo 1. Leia quatro caracteres
letra1, letra2, letra3, letra4 = map(str, input().split())
# Passo 2. Verifique se os caracteres são do alfabeto
if (letra1.isalpha()) != True:
    soletra = False;
elif letra2.isalpha() != True:
    soletra = False;
elif letra3.isalpha() != True:
    soletra = False;
elif letra4.isalpha() != True:
    soletra = False;
else:
    soletra = True
# Passo 2.1. Verifique se os caracteres estão em ordem
if soletra == True:
    if letra1 < letra2 < letra3 < letra4:
        msg = 'Os caracteres estão em ordem crescente.'
    else:
        msg= 'Os caracteres não estão em ordem crescente.'
else:
    msg= 'Pelo menos um dos caracteres não é do alfabeto'
print('{0:s}'.format(msg))

# pós: (letra1 < letra2 && letra2 < letra3 && letra3 < letra4) and os caracteres
#      estão em ordem crescente) || (Os caracteres nao estao em ordem crescente) 
# fim do módulo principal
