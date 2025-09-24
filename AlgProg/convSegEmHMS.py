#entrada é int que representa segundos
#se dividir por 60 temos minutos e o resto
tempo = int(input("Digite o valor:\n"))
min1 = int(tempo/60)
#segundos será o resto da divisão do tempo por 60
seg = int(tempo%60)
#o min1 tem incluido as horas e os minutos(caso n exato)
#horas vai ser o min1 dividido por 60
horas = int(min1/60)
#minu(minutos) vai ser o resto de min1/60
minu = int(min1%60)

print('{0:d} {1:d} {2:d}'.format(horas, minu, seg))