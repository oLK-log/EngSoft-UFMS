# -*- coding: utf-8 -*-
# Programa: password01.py
# Programador:
# Data: 01/05/2020
# Programa para gerar uma password com num caracteres aleatórios,
# sendo que pelo menos k deles seja um número, outros l sejam letras
# maiúsculas e outros m sinais de pontuação (num > k + l + m). O
# programa deve num, k, l, m e a semente, gerar e imprimir a password.
# início do módulo principal
# declaração dos módulos utilizados
import random
import string
# descrição das variáveis utilizadas
# string password, alfabeto, char
# list lpassword
# int semente, num

# pré: num semente

# Passo 1. Leia a entrada
# Passo 1.1. Leia o número de caracteres da password
num = int(input())
# Passo 1.2. Leia o números de dígitos da password
dig = int(input())
# Passo 1.3. Leia o número de letras maiúsculas
mai = int(input())
# Passo 1.4. Leia o número de sinais de pontuação
pon = int(input())
# Passo 1. Leia a semente
semente = int(input())
random.seed(semente)
# Passo 2. Gere uma password com num caracteres
# Passo 2.1. Inicialize o alfabeto
alfabeto = string.ascii_letters + string.digits + string.punctuation
# Passo 2.2. Gere a string
quaisquer = num - mai - dig - pon
password = ''
for i in range(0, quaisquer):
    char = random.choice(alfabeto)
    password = password + char
for i in range(0, mai):
    char = random.choice(string.ascii_uppercase)
    password = password + char
for i in range(0, dig):
    char = random.choice(string.digits)
    password = password + char
for i in range(0, pon):
    char = random.choice(string.punctuation)
    password = password + char
# Passo 2.3. Transforme a password numa lista
lpassword = list(password)
# Passo 2.5. Embaralhe a lista
random.shuffle(lpassword)
# Passo 2.6. Transforme a lista numa string
password = ''
for char in lpassword:
    password = password + char
# Passo 3. Imprima a password
print(password)

# pós: password and password[i] é um caractere aleatório
# fim do módulo principal