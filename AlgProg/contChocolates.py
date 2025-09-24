#4 tamanhos: enorme-50, grande-20, médio-5 e pequeno-1
#ler numero de chocolates
#calcular o número de caixas
#utilizar o mínimo de caixas
#pensamento: é igual converter segundos para hora/min/seg

#ler numero de chocolates
nchoco = int(input("Qual o número de chocolates?\n"))
#calcular quantas caixas enormes vou ter
qE = int(nchoco / 50)
#calcular quantos chocolates sobram(que n cabem em enormes)
#obs: tem q ser um numero menor que 50
resto = nchoco % 50
#calcular quantas caixas grandes vou ter
qG = int(resto / 20)
#calcular o resto
resto = resto % 20
#calcular quantas caixas médias vou ter
qM = int(resto / 5)
#calcular o resto
#nesse ponto, o resto será a quantidade de caixas pequenas
resto = resto % 5
qP = resto
print(' Caixa      Qtde \n=========== =====\n  Enorme       {0:d}\n  Grande       {1:d}\n  Média        {2:d}\n  Pequena      {3:d}'.format(qE,qG,qM,qP))
