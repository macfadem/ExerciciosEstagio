# Questão 1

indice = 13
soma = 0
k = 0

while (k < indice):
    soma = soma + k
    k = k + 1

# Questão 2

def isFibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

# Questão 3

# a) 1, 3, 5, 7, 9 (Números ímpares)
# b) 2, 4, 8, 16, 32, 64, 128 (Potências de 2)
# c) 0, 1, 4, 9, 16, 25, 36, 49 (Quadrados)
# d) 4, 16, 36, 64, 100 (Quadrados perfeitos de números pares)
# e) 1, 1, 2, 3, 5, 8, 13 (Série de Fibonacci)
# f) 2, 10, 12, 16, 17, 18, 19, 200 (Números que começam com a letra D)


