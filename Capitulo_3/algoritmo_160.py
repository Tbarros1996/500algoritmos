# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 160
# Capitulo 2

"""
Entrar com o valor de x e imprimir y: 
í 1, se x <=1 
y =f(x) 2; 5e 1 <x<_ 2 
x ,se2<x<=3 
x 3 , sex >3  

"""
def funcao (x = float):
    if x<1:
        print ("y é 1")
        return 1
    elif x>=1 and x<=2:
        print("Y é 2")
        return 2
    if x>2 and x <= 3:
        print("y é x ao quadrado")
        return x**2
    else:
        print("y é x ao cubo")
        return x**3

x = float(input("Entre com X: "))
y = funcao(x)
print (y)