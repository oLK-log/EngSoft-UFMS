def sePoli(num):
    bina = bin(num)[2:]
    return bina == bina[::-1]
def maior(n):
    for i in range(n, -1, -1):
        if sePoli(i):
            return i
n = int(input())
print(maior(n))