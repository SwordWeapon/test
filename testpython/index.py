# 1 )Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


def fibonacci_check(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num or num == 0:
        return f"O numero {num} pertence a sequencia de Fibonacci."
    else:
        return f"O numero {num} NaO pertence a sequencia de Fibonacci."


numero = 21
print(fibonacci_check(numero))

# 2)  Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
 def count_a(string):
    count = string.lower().count('a')
    if count > 0:
        return f"A letra 'a' aparece {count} vezes na string."
    else:
        return "A letra 'a' nao aparece na string."

# Teste com uma string
texto = "Apresentacao da analise"
print(count_a(texto))

# 3)
int INDICE = 12, SOMA = 0, K = 1;
enquanto K < INDICE faça {
    K = K + 1;
    SOMA = SOMA + K;
}
imprimir(SOMA);
