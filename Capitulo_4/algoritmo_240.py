# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 240
# Capitulo 4

"""
mplementar um algoritmo para calcular o sen(X). O valor de X deverá ser digitado em graus. O valor do seno de Xserá calculado pela soma dos 10 primeiros ter -
mos da série a seguir:
x 3 x5 x 7
senx = x-----+--+--+...
3! 5! 7!
"""

import numpy as np
from math import *


x = np.deg2rad(float(input('Entre com o valor de X (EM GRAUS): ')))
interacoes = int(input('Entre com o número de termos da expansão: '))
valor_aproximado_seno = 0


for i in range(0,interacoes):
    valor_aproximado_seno += (((-1)**i)/factorial((2**i + 1)))*(x**(2*i+1))
    print(sin(x),valor_aproximado_seno)
print(valor_aproximado_seno)