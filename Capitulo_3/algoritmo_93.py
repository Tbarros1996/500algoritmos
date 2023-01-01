# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 93
# Capitulo 2

"""
Entrar com um número e imprimir a raiz quadrada caso seja positivo e o quadrado caso seja negativo
"""


import math as mt

x = float (input(print("Entre com o Número : ")))

if x >= 0:
    print(mt.sqrt(x))
else:
    print(x**2)
