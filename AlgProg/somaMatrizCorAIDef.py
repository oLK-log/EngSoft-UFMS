# -*- coding: utf-8 -*-
# Programa: somamatf.py
# Programador: Lorran Kaíque (baseado em nossa conversa)
# Data: 08/07/2025
# Este programa lê duas matrizes e calcula a sua soma usando uma função.

def somamat(m, n, p, a, b, c):
    """
    Soma duas matrizes 'a' e 'b' de dimensão m x n e armazena o
    resultado na matriz 'c'.

    Args:
        m (int): Número de linhas.
        n (int): Número de colunas.
        p (int): Parâmetro para segunda dimensão (ignorado na soma, mas presente na interface).
        a (list): A primeira matriz (lista de listas).
        b (list): A segunda matriz (lista de listas).
        c (list): A matriz que receberá o resultado da soma.

    Returns:
        list: A matriz 'c' preenchida com a soma.
    """
    # Laço para percorrer cada linha (de 0 a m-1)
    for i in range(m):
        # Laço para percorrer cada coluna (de 0 a n-1)
        for j in range(n):
            # Soma os elementos da mesma posição e guarda em 'c'
            c[i][j] = a[i][j] + b[i][j]
    
    # Retorna a matriz 'c' que foi modificada
    return c

# --- Bloco Principal do Programa ---
if __name__ == "__main__":
    
    # 1. Ler as dimensões da matriz
    # map(int, input().split()) lê a linha, divide e converte para inteiros
    m, n = map(int, input().split())

    # 2. Inicializar as matrizes
    # Cria uma matriz 'a' com 'm' linhas, onde cada linha é uma lista vazia
    a = [[] for _ in range(m)]
    b = [[] for _ in range(m)]
    # Cria a matriz 'c' com o tamanho correto e preenchida com zeros
    c = [[0 for _ in range(n)] for _ in range(m)]

    # 3. Ler os elementos da primeira matriz 'a'
    for i in range(m):
        # Lê uma linha, divide, converte para inteiros e armazena como uma linha da matriz
        a[i] = list(map(int, input().split()))

    # 4. Ler os elementos da segunda matriz 'b'
    for i in range(m):
        b[i] = list(map(int, input().split()))

    # 5. Chamar a função para calcular a soma
    # Passamos 'n' para o parâmetro 'p', já que as dimensões são iguais
    matriz_soma = somamat(m, n, n, a, b, c)

    # 6. Imprimir o resultado
    print(matriz_soma)