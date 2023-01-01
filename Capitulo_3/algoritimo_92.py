# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 92
# Capitulo 2

"""
Construir um algoritmo que leia dois números e efetue a adição. 
Caso o valor somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8;
caso o valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.
"""

def soma(x,y):
    if x+y > 20:
        print("Maior que 20, logo")
        x_1 = x+y+8
        print(x_1)
        return x_1
        
    elif x+y <= 20:
         x_2 = x+y-8
         print(x_2)
         return x_2


x = float(input(print("Entre com o primeiro valor: ")))
y = float(input(print("Entre com o Segundo valor: ")))
soma(x,y)