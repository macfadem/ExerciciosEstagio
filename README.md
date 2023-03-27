## Questão 1

```python
indice = 13
soma = 0
k = 0

while (k < indice):
    soma = soma + k
    k = k + 1

# A soma será 78

## Questão 2

```python
def isFibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

## Questão 3

# a) 1, 3, 5, 7, 9 (Números ímpares)
# b) 2, 4, 8, 16, 32, 64, 128 (Potências de 2)
# c) 0, 1, 4, 9, 16, 25, 36, 49 (Quadrados)
# d) 4, 16, 36, 64, 100 (Quadrados perfeitos de números pares)
# e) 1, 1, 2, 3, 5, 8, 13 (Série de Fibonacci)
# f) 2, 10, 12, 16, 17, 18, 19, 200 (Números que começam com a letra D)

## Questão 4:

# Quando eles se cruzarem na rodovia, eles estarão no mesmo ponto, logo os dois estarão a mesma distância de Ribeirão Preto.
# Adicionalmente, como o caminhão sai a uma velocidade menor (80km/h) que a do carro (110km/h), e ele deve parar quando passa
# em um pedágio, os dois quando cruzarem estarão mais próximos de Franca, cidade onde o caminhão partiu, do que de Ribeirão.

## Questão 5:

# Em python a função seria extremamente simples:
    ```python
    def invertString(str):
        return str[::-1]

# Em JavaScript:

```javascript
function invertString(str) {
    let inverted = "";
    for (let i = str.length - 1; i >= 0; i--) {
        inverted += str[i];
    }
    return inverted;
}
