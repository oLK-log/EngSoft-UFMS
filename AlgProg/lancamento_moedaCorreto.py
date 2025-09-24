# -*- coding: utf-8 -*-
# Programa: lancamento_moeda.py
# Programador: 
# Data: 21/05/2025 
# Este programa simula repetidamente o lançamento de uma moeda
# para calcular a média de prêmios em um jogo específico,
# onde o prêmio é 2 * n, sendo n o número da jogada na qual a primeira cara aparece.

import random

# Passo 0: Iniciar variáveis
soma_dos_premios = 0.0
NUM_JOGADAS_SIMULADAS = 100 # Número de vezes que o jogo será simulado

# Passo 1: Ler a semente
try:
    semente = int(input())
    random.seed(semente) # Inicializa o gerador de números pseudoaleatórios com a semente
except ValueError:
    print("Erro: A semente deve ser um número inteiro.")
    exit() # Encerra o programa se a entrada for inválida

# Passo 2: Simular as 100 jogadas do jogo
for _ in range(NUM_JOGADAS_SIMULADAS):
    n = 0 # Inicializa o contador de lançamentos para esta rodada
    primeira_cara_encontrada = False

    while not primeira_cara_encontrada:
        n += 1 # Incrementa o contador de lançamentos

        # === CORREÇÃO NA SIMULAÇÃO DA MOEDA ===
        # Simula o lançamento da moeda: 0 para Cara, 1 para Coroa (ou vice-versa)
        # random.randint(0, 1) garante 50% de chance para cada.
        # Vamos considerar 0 como "Cara"
        resultado_lancamento = random.randint(0, 1)

        if resultado_lancamento == 0: # Se o resultado for 0 (Cara)
            primeira_cara_encontrada = True
            premio_da_rodada = 2 * n # Calcula o prêmio para esta rodada (2 multiplicado por n)
            soma_dos_premios += premio_da_rodada # Adiciona o prêmio à soma total
        # ======================================

# Passo 3: Calcular a média dos prêmios
media_premios = soma_dos_premios / NUM_JOGADAS_SIMULADAS

# Passo 4: Imprimir a média dos prêmios formatada (duas casas decimais)
print(f"{media_premios:.2f}")