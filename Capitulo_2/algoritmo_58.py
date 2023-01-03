# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 58
# Capitulo 2
"""
Entrar com valores para xnum 1, xnum2 e xnum3 e imprimir o valor de x, sabendo-se que:
X = xnuml +
xnum2
+ 2(xnuml - xnum2) + 1 og 264
xnum3 + xnuml

(Olhe o Livro)

"""

from math import *

def formu(x1 = float, x2 = float, x3 = float):
    x = x1 + (x2/(x3+x1)) + 2*(x1-x2) + log10(64)/log10(2)
    print(f"O Valor de X é: {x}")

formu(1,2,3)