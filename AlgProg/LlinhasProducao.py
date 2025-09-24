# -*- coding: utf-8 -*-
# Programa: LlinhasProducao
# Programador: Lorran Kaíque
#Este programa
import math
# numero de estado- est = 2**q
#Para simular 1 q precisa de 2 bits, 2-4, 3-8, 4-16
#1MB = 10**6 bytes
#1 byte = 8 bits
#Entrada- M representa a quantidade de MB
#Ler entrada
MB = int(input())
#Converter bytes em bites
bites = 8*(MB*(10**6))
#achar o valor de vezes que 2 será multiplicado
#tem que fazer log
naturalBites = math.log(bites)
naturalBase = math.log(2)
resultado = math.ceil(naturalBites / naturalBase)
print('{0:.0f}'.format(resultado))