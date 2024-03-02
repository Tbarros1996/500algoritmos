# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 225
# Capitulo 4

"""
Criar um algoritmo que entre com uma palavra e imprima conforme o exemplo a
seguir:
palavra: 

A
RA
RRA
ERRA
TERRA

"""

nome = str(input("Entre com o Nome: "))

for x in range(0, len(nome),1):
    print(nome[-x-1:])
    
