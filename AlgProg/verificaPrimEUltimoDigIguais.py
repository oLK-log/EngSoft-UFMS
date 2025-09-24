#ver se o primeiro e o útimo dígito são iguais
#entrada é int
#saída é "sim" caso sejam iguais e "não" caso oposto
#regras: o numero n pode ser lido como str
#deve ser resolvido com operaçao de divisao e resto

#entrada n inteiro
number = int(input("Digite um número:\n"))
#obter o último dígito:
end = number % 10
#obter o primeiro dígito:
cont = number
while cont >= 10:
    cont //=10
first = cont
#ver se sao iguais
if first == end:
    print("sim")
else:
    print("não")