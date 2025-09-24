#receber um número binário de até 3 dígitos e converter para decimal
#não pode ser utilizado if,for,while
#pensamento: a conversão de um núumero binário considera a casa
#ex:110-da direita para a esquerda o 0 equilave a casa de valor 1, como é 0 é nulo
#a segunda casa equivale a casa de valor 2, como é 1 então o contador tem 2
#a 3° casa equivale ao valor 4, como é 1 então o contador recebe mais 4, logo c = 6
#seria o digíto*valorCasa: 0*1 + 1*2 + 1*4

#entrada
nu = int(input("Digite o número em binário com até 3 casas:\n"))
binario = nu
#achar o dígito em binário
dig1 = nu % 10
nu //=10
dig2 = nu %10
nu //=10
dig3 = nu
#converter em dec
decimal = dig1 * 1 + dig2 * 2 + dig3 * 4
#imprimindo
print('{0:d} (base 2) == {1:d} (base 10)'.format(binario, decimal))

    