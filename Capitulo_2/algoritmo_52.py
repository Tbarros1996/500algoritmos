# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 52
# Capitulo 2
"""
Entrar com os lados a, b, c de um paralelepípedo. Calcular e imprimir a diagonal.
"""

def paralele(a = float, b = float, c = float):
    diagonal = ((a**2)+(b**2)+(c**2))**(0.5)
    print("A diagonal é: ", diagonal)

paralele(1,2,3)