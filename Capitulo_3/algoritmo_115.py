# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro  
# 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 115
# Capitulo 2


"""
Criar o algoritmo que deixe entrar com dois números e imprimir o quadrado do
menor número e a raiz quadrada do maior número, se for possível.

"""
from cmath import *

x = float(input(print("Entre com o X1\a : ")))
y = float(input(print("Entre com o X2\a : ")))
def teste(x,y):
    if x>y:
        print(sqrt(x),y**2)
    if y>x:
        print(sqrt(y),x**2)
    if x == y:
        print("Numeros Iguais")
teste(x,y)