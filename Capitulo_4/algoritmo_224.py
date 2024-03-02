# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 224
# Capitulo 4

"""
Criar um algoritmo que entre com uma palavra e imprima conforme o exemplo a
seguir:
palavra: AMOR
AMOR
AMO
AM
A
"""

nome = str(input("Entre com o Nome: "))

for x in range(len(nome),0,-1):
    print(nome[:x])
    
