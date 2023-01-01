# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 120
# Capitulo 2

"""
Entrar com três números e armazená-los em três variáveis com os seguintes no-
mes maior, intermediário e menor (suponha numeros diferentes)

"""

x = float(input(print("Entre com o X1\a : ")))
y = float(input(print("Entre com o X2\a : ")))
z = float(input(print("Entre com o X3\a : ")))

lista = [x,y,z]
lista_ordenada = sorted(lista)
menor = lista_ordenada[0]
intermediario = lista_ordenada[1]
maior = lista_ordenada[2]

print(f'O menor é {menor}, o intemediário é {intermediario}, e o maior é {maior}')