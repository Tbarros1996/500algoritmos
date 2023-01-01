# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 116
# Capitulo 2

"""
Entrar com três números e imprimir o maior número (suponha números diferentes).
"""
x = float(input(print("Entre com o X1\a : ")))
y = float(input(print("Entre com o X2\a : ")))
z = float(input(print("Entre com o X3\a : ")))
def teste(x,y,z):
    if x>y and x>z:
        print(x)
    elif y>x and y>z:
        print(y)
    elif z>y and z>x:
        print(z)
    if x==y==z:
        print("Todos iguais")
        
teste(x,y,z)