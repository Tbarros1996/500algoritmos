# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 186
# Capitulo 4

"""
Entrar com quatro números e imprimir o cubo e a 
raiz cúbica de cada número. 

"""

import math as mt

for i in range(0,15):
    x = int(input('Entre com o valor'))
    if x>0:
        y = mt.sqrt(x)
        print(y)
    else:
        print('Raiz real de negativo não existe')