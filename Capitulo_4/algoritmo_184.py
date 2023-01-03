# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 184
# Capitulo 4

"""
Entrar com 8 números e, para cada número, 
imprimir o logaritmo desse número 
na base 10. 

"""

import math as mt

for i in range(0,8):
    x = int(input('Entre com o valor'))
    if x>0:
        y = mt.log10(x)
        print(y)
    else:
        print('Log não possui valor para n negativo')