# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 42
# Capitulo 2
"""
Entrar com um ângulo em graus e imprimir: seno, co-seno, tangente, secante,
co-secante e co-tangente deste ângulo.
"""

import math as mt

angulo_radiano = input(print("Entre com o Angulo: ")) 
angulo_radiano = (float(angulo_radiano)*mt.pi)/180

seno = mt.sin(angulo_radiano)
print(round(seno,3) )
cosseno = mt.cos(angulo_radiano)
print(cosseno)
tangente= mt.tan(angulo_radiano)
print(tangente)
secante= 1/(mt.cos(angulo_radiano))
print(secante)
cossecante= 1/(mt.sin(angulo_radiano))
print(cossecante)
cotangente= 1/(mt.tan(angulo_radiano))
print(cotangente)





