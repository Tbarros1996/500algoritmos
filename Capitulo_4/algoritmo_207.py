# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 207
# Capitulo 4


"""
Sabendo-se que a UAL calcula o produto através de somas sucessivas, criar um algoritmo
que calcule o produto de dois números inteiros lidos. Suponha que os
números lidos sejam positivos e que o multiplicando seja menor do que o multiplicador.

"""

num1 = int (input('Entre com o multiplicando: '))
num2 = int (input('Entre com o multiplicador: '))
soma = 0
for i in range(1, num2+1):
    soma = soma + num1
print("E o produto é : ", soma)

