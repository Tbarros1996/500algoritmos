# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 187
# Capitulo 4

"""
Criar um algoritmo que calcule e imprima o 
valor de b^n. 
O valor de n deverá ser maior do que 1 e 
inteiro e o valor de b maior ou igual a 2 
e inteiro.  

"""
base = int(input('Entre com o a base maior que 1: '))
expoente = int(input('Entre com o expoente maior que 1: '))


if base >=2 and expoente >=2:
    i = 0
    for i in range(i,expoente):
        potencia = base**expoente
        print(potencia)
else:
    print("Condição não Satisfatória")


# Repeticição acima dos 4300 no python será necessário exceder 
# com o módulo sys