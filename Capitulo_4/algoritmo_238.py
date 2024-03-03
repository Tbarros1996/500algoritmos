# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 238
# Capitulo 4

"""
Ler o numero de termos da serie (N) e imprimir o valor de S sendo
"""

num = int(input('Entre com o Número: '))
h = 0
n = num

for c in range(1,num+1):
    h += (h + c)/n
    n += n -1
    print(c,h,n)


