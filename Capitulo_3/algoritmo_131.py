# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 131
# Capitulo 2

"""
A turma de Programação 1, por ter muitos alunos, será dividida em dias de provas.
Após um estudo feito pelo coordenador, decidiu-se dividi-la em três grupos.
Fazer um algoritmo que leia o nome do aluno e indicar a sala em que ele deverá
fazer as provas, tendo em vista a tabela a seguir e sabendo-se que todas as salas
se encontram no bloco F
A - K:sala 101
L-N:sala 102
O - Z:sala 103
"""

# A maneira mais simples é a entrada da letra do primeiro nome usando

import string
nome = str(input("Entre com a primeira letra do seu nome: "))
maiusculo = list(string.ascii_uppercase)
minusculo = list(string.ascii_lowercase)
A_K= maiusculo[0:11]
L_N= maiusculo[12:14]
O_Z= maiusculo[15:]
a_k=minusculo[0:11]
l_n=minusculo[12:14]
o_z=minusculo[15:]
            
if nome in A_K or nome in a_k:
    print("Dirija-se a sala 101")
elif nome in L_N or nome in l_n:
    print("Dirija-se a sala 102")
elif nome in O_Z or nome in o_z:
    print("Dirija-se a sala 103")
