# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 159
# Capitulo 3

"""
Entrar com o valor de x e imprimir y: 
Olhar no livro

"""

import math as mt

x = float (input("Entre com o valor de x: "))
nume = 5*x+3
deno = mt.sqrt(x**2 - 16)

if x>4 or x < (-4):
    y = nume/deno
    print(y)
elif x**2 < 16:
    print("Sem solução real")