# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 113
# Capitulo 2



"""
Entrar com dois números e imprimir em ordem crescente

"""
x = float(input(print("Entre com o X1\a : ")))
y = float(input(print("Entre com o X2\a : ")))
def teste(x,y):
    if x>y:
        print(y,x)
    if y>x:
        print(x,y)
teste(x,y)