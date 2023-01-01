# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 119
# Capitulo 2

"""
Entrar com três números e imprimi-los em ordem decrescente (suponha números di -
ferentes).

"""

x = float(input(print("Entre com o X1\a : ")))
y = float(input(print("Entre com o X2\a : ")))
z = float(input(print("Entre com o X3\a : ")))

lista = [x,y,z]
lista_ordenada = sorted(lista)
print(lista_ordenada[2],lista_ordenada[1],lista_ordenada[0])

# A ultima linha pode ser também

print(lista_ordenada[::-1]) # Fazendo um slice