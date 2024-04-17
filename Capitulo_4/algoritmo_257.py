# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 257
# Capitulo 4

"""
Criar um algoritmo que leia o valor de N imprima a sequência a seguire o resultado

N! 1021
 (N_1)i1221 + ( N_2)i/421 _(N_3)i/6 2 I +
 0!
 (2N2)!
"""


from math import *

soma = 0
n = int(input('Entre Com o valor de N: '))
i = int(input('Entre com a Quantidade de Termos: '))


for k in range(i):
    
    if k % 2 == 0:
        termo = factorial(n-k)/factorial(2 * (k**2))
        soma += termo
        
    else:
        termo = factorial(n-k)/factorial(2 * (k**2))
        soma -= termo

print(f'A soma é de {round(soma,2)}')