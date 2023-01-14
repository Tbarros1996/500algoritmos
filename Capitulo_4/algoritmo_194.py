# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 194
# Capitulo 4

"""
Criar um algoritmo que leia um número e imprima todos os números de 1 até o 
número lido e o seu produto.

"""
ls =int(input("Entre com a Limite Superior: "))
i = 1
for contador in range(1,ls+1,1):
    produto = contador * i
    i = produto
    print(produto)