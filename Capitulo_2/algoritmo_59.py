# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 59
# Capitulo 2
"""
Entrar com os valores dos catetos de um triângulo retângulo e imprimira hipotenusa

"""

from math import *

def hipo(cat1 = float, cat2 = float):
    hipo = sqrt(cat1**2+cat2**2)
    print(f"A hipotenusa é: {hipo}")

hipo(3,4)
