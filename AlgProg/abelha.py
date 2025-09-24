# -*- coding: utf-8 -*-
# Programa: abelha.py
# Programador:
# Data: 12/10/2011
# Numa rua de oito quadras, a loja de conveniência está na quadra 8, e uma
# loja de doces na quadra 1. Uma abelha começa na quadra n, 1 < n < 8, e
# vagueia aleatoriamente, uma quadra de cada vez, em direção a loja de
# conveniência ou em direção a loja de doces. Em cada esquina, ela se move
# em direção da loja de doces com uma determinada probabilidade,
# digamos 2/3, e em direção a loja de conveniência com uma determinada
# probabilidade, digamos 1/3. Chegando a loja de conveniência ou a loja
# de doces, ela permanece lá. Escreva um programa para simular 500 voos
# na qual ela começa na quadra 2, outras 500 na qual ela começa na quadra 3,
# e assim por diante até a quadra 7. Para cada ponto inicial, calcule e
# imprima a probabilidade das vezes que ela termina na loja de conveniência,
# a probabilidade das vezes que ela termina na loja de doces, e a média do
# número de quadras que ela voa em cada tentativa.
# declaração dos módulos utilizadas
import random
# início do módulo principal
# descrição das variáveis locais
# int     quadrai
# float   lojadoces, lojaconv, media
# int     quadra, voo
# int     numldoces, numlconv, numquadras
# int     semente

# pré: semente, quadrai

# Passo 1. Leia/gere a entrada
# Passo 1.1. Leia a semente
semente = int(input())
# Passo 1.2. Gere a sequência de números aleatórios
random.seed(semente)
# Passo 2 Iniciando na quadra quadrai
for quadrai in range(2, 8):
    # Passo 2.1. Inicialize as variáveis
    numldoces = 0
    numlconv = 0
    total_quadras = 0

    # Passo 2.2. Simule 500 caminhadas começando em quadrai
    for i in range(0, 500):
        quadra = quadrai
        voo = 0
        # Passo 2.2.1. Enquando a abelha não chegar na conveniência ou lj de doces faça
        while quadra != 1 and quadra != 8:
            # Passo 2.2.1.1. Gere a direção a ser tomada (2/3 lj doces 1/3 conv)
            # 0 caminho da conveniência
            # 1 e 2 caminho da lj de doces
            direcao = random.randint(0, 2)
            if direcao < 2:  # Move para a loja de doces (probabilidade 2/3)
                quadra -= 1
            else:  # Move para a loja de conveniência (probabilidade 1/3)
                quadra += 1
            # Passo 2.2.1.2. Compute o número de quadras voadas
            voo += 1

        # Passo 2.2.2. Se a abelha chegou na lj de doces
        if quadra == 1:
            numldoces += 1
        # Passo 2.2.3. Se a abelha chegou na conveniência
        elif quadra == 8:
            numlconv += 1
        # Passo 2.2.4. Compute o total de quadras voadas até i
        total_quadras += voo

    # Passo 2.3. Compute a probabilidade que a abelha chegou na lj doces
    lojadoces = numldoces / 500.0
    # Passo 2.4. Compute a probabilidade que a abelha chegou na conveniência
    lojaconv = numlconv / 500.0
    # Passo 2.5. Compute a média de quadras voadas por trajeto
    media = total_quadras / 500.0
    # Passo 2.6. Imprima os resultados
    print('{0:d} {1:.6f} {2:.6f} {3:.6f}'.format(quadrai, lojadoces, lojaconv, media))

# pós: lojadoces and lojadoces == prob que a abelha chegou na loja de doces
#     lojaconv and lojaconv == prob que a abelha chegou na conveniência
#     media and media == média de quadras voadas
# fim do módulo principal