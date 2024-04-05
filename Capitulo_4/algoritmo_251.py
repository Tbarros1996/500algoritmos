# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 251
# Capitulo 4

"""

Criar um algoritmo para imprimir uma tabela para DEZ times num torneio de ro-
dada dupla.

"""


for i in range(1,11):
    for j in range(1,11):
        if i != j:
            print(f'Time: {i} x Time {j} ')