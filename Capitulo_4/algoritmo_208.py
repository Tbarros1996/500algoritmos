# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 208
# Capitulo 4


"""
Criar um algoritmo que imprima os 10 primeiros termos da série de firbonacci.

Obs: os dois primeiros termos desta série são 1 e 1 e os demais são gerados a partir da soma dos anterior.


"""


firbonacci = [1,1]
x = int(input('Entre com a quantidade de termos de firbonacci que deseja que seja retornada'))
i = 0
while i < x:
    soma = firbonacci[i] + firbonacci[i + 1]
    firbonacci.append(soma)
    i += 1

print(f'A sequencia de firbonacci para os {i}° Termos é: ')
print(firbonacci)
