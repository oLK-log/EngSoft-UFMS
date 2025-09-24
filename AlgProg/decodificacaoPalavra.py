# -*- coding: utf-8 -*-
# Programa: codifica00.py
# Programador: Lorran Kaíque Silveira Fernandes
# Data: 26/04/2025
#Decodifica uma palavra usando a técnica de "Deslocamento"
#Passo 0- iniciar variaveis
res = ""
#Passo 1. Ler as entradas
#Passo 1.1 Ler a palavra
pal = input()
#Passo 1.2 Ler o número de deslocamento
n = int(input())
#Passo 2- loop de decodificação
for letra in pal:
    res += chr((ord(letra)-n-65)% 26 + 65)
print(res)
#Pós:
#ord(letra): retorna o cod da letra atual
#ord(letra) - n : deslocamento é subtraido do código
#"-65": ajusta o cálculo para iniciar do índice 0
#obs-(a contagem inicia em 65 pelo A)
#"%26": garante que o cod permanecerá no intervalo alfabetico(25letras)
#"+65":converte para o intervalo alfabetico
#chr: converte o cod para caracter