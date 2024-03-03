# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 236
# Capitulo 4

"""
Ler o numero de termos da serie (n) e imprimir o valor de H sendo
"""

final = int(input('Entre com o valor de n: '))

N = 0

for i in range(1,final+1):
    if i % 2 == 0:
        N += (1/i)*(-1)
        print(N,i)
    else:
        N += (1/i)
        print(N,i)

