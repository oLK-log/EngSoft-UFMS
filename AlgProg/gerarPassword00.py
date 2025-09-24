# -*- coding: utf-8 -*-
# Programa: password00.py
# Programador:
# Data: 01/05/2020
# Programa para gerar uma password com 8 caracteres aleatórios,
# sendo que pelo menos um deles seja um número, outro uma letra
# maiúscula e outro um sinal de pontuação. O programa deve
# ler a semente, gerar e imprimir o a password.
# início do módulo principal
# declaração dos módulos utilizados
import random
import string
# descrição das variáveis utilizadas
# string password, alfabeto, char
# list lpassword
# int semente

# pré: semente

# Passo 1. Leia a semente
semente = int(input())
random.seed(semente)
# Passo 2. Gere uma password com 8 caracteres
# Passo 2.1. Inicialize o alfabeto
alfabeto = string.ascii_letters+string.digits+string.punctuation
# Passo 2.2. Inicialize a password
password = ''
# Passo 2.3. Gere 5 caracteres aleatórios do alfabeto
for i in range(0,5):
   char = random.choice(alfabeto)
# Passo 2.3.1. Concatene o caractere na password
   password += char
# Passo 2.4. Gere uma letra maiúscula aleatória
char = random.choice(string.ascii_uppercase)
# Passo 2.5. Concatene a letra na password
password += char
# Passo 2.6. Gere um dígito aleatório
char = random.choice(string.digits)
# Passo 2.7. Concatene o dígito na password
password += char
# Passo 2.8. Gere um sinal de pontuação aleatório
char = random.choice(string.punctuation)   
# Passo 2.9. Concatene o sinal na password
password += char
# Passo 2.10. Transforme a string numa lista
lpassword = list(password)
# Passo 2.11. Embaralhe os elementos da lista
random.shuffle(lpassword)
# Passo 2.12. Transforme a lista numa string
password = ''
for char in lpassword:
   password = password + char
# Passo 3. Imprima a password
print(password)

# pós: password and password[i] é um caractere aleatório
# fim do módulo principal