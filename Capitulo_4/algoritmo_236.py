# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 236
# Capitulo 4

"""
Ler o numero de termos da serie (n) e imprimir o valor de H sendo
"""

n = int(input('Entre com o valor de n: '))

H = 0

for i in range(1,n+1):
    H += (1/i)
    print(i,H)