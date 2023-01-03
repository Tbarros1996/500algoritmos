# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 50
# Capitulo 2
"""
Entrar com a base e a altura de um retângulo e imprimir a seguinte saída:
peri metro
area
diagonal:

"""

import math as mt
def retangulo(base = float, altura = float):
    perimetro = 2*(base+altura)
    area = base*altura
    diagonal = mt.sqrt((base**2)+(altura**2))
    print("O valor do Perimetro é: ", perimetro)
    print("O valor da Área é: ", area)
    print("O valor da Diagonal é: ", diagonal)

retangulo(2,3)
