# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 65
# Capitulo 2
"""
Calcular e apresentar o valor do volume de uma lata de óleo, 
utilizando a fórmula:volume = 3.14159 * R2 * altura.

"""

from math import *

def cvolume(altura = float,raio = float):
    volume = pi * (raio**2) *altura
    print(f"O Volume é {volume}")
    return volume

volume = cvolume(1,2) 