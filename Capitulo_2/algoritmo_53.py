# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 53
# Capitulo 2
"""
Entrar com o lado de um quadrado e imprimir: 
perimetro: 
area: 
diagonal: 

"""

import math as mt
def quadrado(l = float):
    perimetro = 4*l
    area = l**2 
    diagonal = l*mt.sqrt(2)
    print("O valor do Perimetro é: ", perimetro)
    print("O valor da Área é: ", area)
    print("O valor da Diagonal é: ", diagonal)

quadrado(2)