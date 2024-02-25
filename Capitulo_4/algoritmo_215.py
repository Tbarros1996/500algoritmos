# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 215
# Capitulo 4

"""
Entrar com o número e imprimir todos os seus divisores

"""

import time as tm
import pandas as pd
x = int(input("Entre com o Valor: "))

for i in range(1, x+1):
    if x % i == 0:
        print(i)

