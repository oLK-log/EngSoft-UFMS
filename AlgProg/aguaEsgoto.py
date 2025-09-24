# -*- coding: utf-8 -*-
# Programa: aguaesgoto.py
# Programador: Lorran Kaíque Silveira Fernandes
# Data: 27/04/2025
# Este programa lê o consumo de água de uma residência
# e calcula a fatura da conta de água e esgoto para as 
# residência baseada no consumo de agua. O programa lê o código
# da residência (consumidor), o consumo de água da residência, computa 
# a fatura e então imprime uma fatura com o código do consumidor e os 
# valores cobrados com mensagens apropriadas. 
# início do módulo principal
# descrição das variáveis utilizadas
# int cod_consumidor, consumo
# float fat_agua, fat_esgoto, fat_total

# pré: cod_consumidor consumo

# Passo 1. Leia o código do consumidor e consumo de água
cod_consumidor = int(input())
consumo = int(input())
#Passo 1.1- Inicializar variaveis
fat_agua = 0
restante = consumo
# Passo 2. Calcule valor da fatura
if consumo <= 20:
    fat_agua = consumo*2.07
    fat_esgoto = fat_agua*0.70
elif consumo <= 25:
    fat_agua += 10*4.45
    restante -= 10
    fat_agua += 5 * 5.79
    restante -= 5
    fat_agua += 5*5.91
    restante -= 5
    fat_agua += restante * 6.54
    
elif consumo <= 30:
    fat_agua += 10*4.45
    restante -= 10
    fat_agua += 5 * 5.79
    restante -= 5
    fat_agua += 5 * 5.91
    restante -= 5
    fat_agua += 5 * 6.54
    restante -= 5
    fat_agua += restante*8.01
    
elif consumo <= 50:
    fat_agua += 10 * 4.45
    restante -= 10
    fat_agua += 5 * 5.79
    restante -= 5
    fat_agua += 5 * 5.91
    restante -= 5
    fat_agua += 5 * 6.54
    restante -= 5
    fat_agua += 5 * 8.01
    restante -= 5
    fat_agua += restante*9.63

else:
    fat_agua += 10 * 4.45
    restante -= 10
    fat_agua += 5 * 5.79
    restante -= 5
    fat_agua += 5 * 5.91
    restante -= 5
    fat_agua += 5 * 6.54
    restante -= 5
    fat_agua += 5 * 8.01
    restante -= 5
    fat_agua += 30*9.63
    restante -= 30
    fat_agua += restante * 10.78
# Passo 2.2. Calcule o valor do esgoto
fat_esgoto = fat_agua*0.70
# Passo 2.3. Calcule o fatura total
fat_total = fat_agua + fat_esgoto
# Passo 3. Imprima os resultado
print('===========================================')
print('Água e Esgotos Pureza e Limpeza Total Ltda.')
print('Consumidor: {0}'.format(cod_consumidor))
print('Consumo de Água: {0}'.format(consumo))
print('Valor da Água  : R${0:8.2f}'.format(fat_agua))
print('Valor do Esgoto: R${0:8.2f}'.format(fat_esgoto))
print('Valor Total    : R${0:8.2f}'.format(fat_total))
print('===========================================')

# pós: fat_total = fat_agua + fat_esgoto
# fim do módulo principal
