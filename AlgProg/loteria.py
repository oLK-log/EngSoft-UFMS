# -*- coding: utf-8 -*-
# Programa: randomsample00.py
# Programador:
# Data: 01/05/2020
# Programa para demonstrar a utilização da função sample(). O
# programa gera 1000 números inteiros de um bilhete de loteria
# variando entre 000001 e 999999, sorteia os 5 primeiros
# prêmios e imprime a lista dos bilhetes sorteados.
# início do módulo principal
# declaração dos módulos utilizados
import random
# descrição das variáveis utilizadas
# list loteria, premios
# int semente

# pré: semente

# Passo 1. Leia a semente
semente = int(input())
random.seed(semente)
# Passo 2. Simule o sorteio de uma loteria
# Passo 2.1. Gere 1000 bilhetes de loteria
loteria = random.sample(range(1,99999),1000)
# Passo 2.2. Sorteie os 5 bilhetes premiados
premios = random.sample(loteria,5)
# Passo 3. Imprima a lista
print(premios)

# pós: premios and premios[i] selecionado aleatoriamente
# fim do módulo principal
import random

semente = int(input())
random.seed(semente)

# Gere números de bilhetes de 6 dígitos (de 100000 a 999999)
intervalo_6_digitos = range(100000, 1000000)

# Verifique se há pelo menos 1000 números únicos disponíveis
if len(intervalo_6_digitos) >= 1000:
    loteria = random.sample(intervalo_6_digitos, 1000)
    premios = random.sample(loteria, 5)
    print(premios)
else:
    print("Não há números únicos suficientes de 6 dígitos para gerar 1000 bilhetes.")