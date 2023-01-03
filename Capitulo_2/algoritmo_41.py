# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 41
# Capitulo 2
"""

Entrar com quatro números e imprimir a média ponderada, sabendo-se que os
pesos são respectivamente: 1, 2, 3 e 4

"""
import math as mt
n1 = int(input(print("Entre com o VALOR 1:\n")))
n2 = int(input(print("Entre com o VALOR 2:\n")))
n3 = int(input(print("Entre com o VALOR 3:\n")))
n4=  int(input(print("Entre com o VALOR 4:\n")))

media_po = (n1*1 + n2*2 + n3*3 + n4*4)/(mt.factorial(4))

print("\n")
print("Media Ponderada é"), print("\n"), print(media_po)