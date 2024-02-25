# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 211
# Capitulo 4

"""
Criar um algoritmo que imprima todos os números inteiros positivos no intervalo aberto entre 10 e 110 de forma que:

não terminem em zero de forma que;

- Não terminem em zero
- se o dígito da direita for removido, o número restante é divisor do número original

Ex:26: 2 é divisível por 26


"""

for x in range(11,100):
    if x % 10 == 0:
        pass
    elif x % 10 != 0:
        valor_inteiro = x//10
        if x % valor_inteiro == 0:
            print(x)
        else:
            pass
        