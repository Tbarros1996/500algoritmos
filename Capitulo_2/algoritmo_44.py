# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 44
# Capitulo 2


"""
Entrar com o número e a base em que se deseja calcular o logaritmo desse número e imprimi-lo.
"""

import math as mt

logaritimando = float(input(print("Entre com o Logaritimando: ")))
print('\a')
base = float(input(print("Entre com a Base: ")))
print('\a')
logaritmo = mt.log10(logaritimando)/mt.log10(base)
print(logaritmo)
