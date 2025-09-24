#SomaParImpar
#ler dois numeros inteiros mesma linha
#representam o inicio e o fim de uma sequencia de numeros
#calcule a soma dos numeros impares
#inclui inicio e fim
numbers = str(input("Digite dois numeros:\n"))
start, end = numbers.split(" ")
start = int(start)
end = int(end)
x= start
y = 0
end = int(end)

while x != (end+1):
    if x % 2 != 0:
        y += x
    x += 1

print(y)