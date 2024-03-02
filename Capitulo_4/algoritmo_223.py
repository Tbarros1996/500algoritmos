# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 223
# Capitulo 4

"""
Criar um algoritmo que entre com uma palavra e imprima conforme o exemplo a
seguir:
palavra: AMOR
A
AM
AMO
AMOR

"""

nome = str(input("Entre com o Nome: "))

for x in range(1,len(nome)+1):
    print(nome[:x])