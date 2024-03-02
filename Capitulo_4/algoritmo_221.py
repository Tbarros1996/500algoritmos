# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 221
# Capitulo 4

"""
Criar um algoritmo que entre com uma 
palavra e imprima conforme o exemplo a
seguir:
input:PAZ
Output:
P
A
Z
"""

nome = str(input("Entre com o Nome: "))

# Método 1

for i in range(0,len(nome)):
    print(nome[i])


# Método 2

lista = list(nome)

for x in range(0,len(nome)):
    print(lista[x])