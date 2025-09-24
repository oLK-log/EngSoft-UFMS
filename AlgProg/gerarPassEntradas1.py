# -*- coding: utf-8 -*-
# Programa: password01.py
# Programador:Lorran Kaíque
# Data: 15/05/2025
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
password = ''
#Passo 3. Inicie as iterações
#Passo 3.1- gerar os digtos
for i in range(0, dig):
    char = random.choice(string.digits)
    password += char
num -= dig
#Passo 3.2- gerar maiúsculas
for i in range(0, mai):
    char = random.choice(string.ascii_uppercase)
    password += char
num -= mai
#Passo 3.3- gerar caracteres especiais(pon)
for i in range(0, pon):
    char = random.choice(string.punctuation)
    password += char
num -+ pon
#Passo 3.4- gerar restante dos caracteres
for i in range(0, num):
    char = random.choice(alfabeto)
    password += char
#Passo 4- Imprimir
#Passo 4.1- Transformar a password numa lista
lpassword = list(password)
#Passo 4.2- Embaralhar a lista
random.shuffle(lpassword)
#Passo 4.3- Transforma a lista em uma string
password = ''
for char in lpassword:
    password = password + char
#Passo 4.5- Imprimir
print(password)
# pós: password and password[i] é um caractere aleatório
# fim do módulo principal
