/*

Questão 4:

Quando eles se cruzarem na rodovia, eles estarão no mesmo ponto, logo os dois estarão a mesma distância de Ribeirão Preto.
Adicionalmente, como o caminhão sai a uma velocidade menor (80km/h) que a do carro (110km/h), e ele deve parar quando passa
em um pedágio, os dois quando cruzarem estarão mais próximos de Franca, cidade onde o caminhão partiu, do que de Ribeirão.

Questão 5:

 Em python a função seria extremamente simples:
    def invertString(str):
        return str[::-1]
*/
function invertString(str) {
    let inverted = "";
    for (let i = str.length - 1; i >= 0; i--) {
        inverted += str[i];
    }
    return inverted;
}