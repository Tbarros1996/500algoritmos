# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 214
# Capitulo 4

"""
Entrar com o nome o nome, nota da PR1 e nota da PR2
de 15 alunos. Imprimir uma listagem, contendo: nome, nota da PR1
nota da PR2, e média arredondada de cada aluno.

Ao final, calcule a média geral da turma

"""
import numpy as np

nome = []
pr1 = []
pr2=[]

for i in range(1,4):
    nome.append(input("Entre com o Nome: "))
    pr1.append(round(float(input("Entre com  a PR1: "))),2)
    pr2.append(round(float(input("Entre com a PR2: "))),2)
    
media = (np.array(pr1)+np.array(pr2))/2
print(f'Nome: {nome}, Media: {media}')