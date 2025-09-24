# -*- coding: utf-8 -*-
# Programa: seqCheia.py
# Programador: Lorran Kaique
# Data: 03/06/25
#Este programa le uma sequencia de numeros e determina se ela é CHEIA
#sequencia cheia: a diferença entre os consecultivos entá contida na sequencia
#valor absoluto = n[1]-n[0]
#Passo 0: Inicializar as variaveis
abso = [] #inicializando list de absolutos
msg = "N"
x = 0
#Passo 1: Ler sequencia
tam = int(input())
seq = list(map(int, input().split()))
#Passo 2: Achar valores absolutos
#Passo 2.2 iterar entre consecultivos
for i in range(0, tam-1):
    valor = seq[(i+1)] - seq[i]
    if valor < 0:
        valor *=-1
    abso.append(valor)
#Passo 3. Verificar se sequencia
    setCalc = set(abso)
    esperado = set()
    if tam > 1:
        for i in range(1, tam):
            esperado.add(i)
    if tam > 1 and setCalc == esperado:
        msg = "C"
        
    else:
        msg = "N"
#Passo 4. Imprimir
print(msg)
