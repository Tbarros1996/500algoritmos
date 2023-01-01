# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 101
# Capitulo 2


"""
Construir um algoritmo que indique se o número digitado está compreendido en-
tre 20 e 90 ou não.

"""

valor = float(input(print("Entre com o valor ")))

if valor >= 20 and valor <= 90:
    print("O valor está entre 20 e 90")
elif valor < 20:
    print("O valor é menor que 20")
else:
    print("O valor é maior que 90")
    