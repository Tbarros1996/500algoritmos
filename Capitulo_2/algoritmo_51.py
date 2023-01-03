# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 51
# Capitulo 2
"""
Entrar com o raio de um cfrculo e imprimir a seguinte saída:
peri metro:
area:
"""

def circe(lado = float):
    perimetro = lado*4
    area = lado*lado
    diagonal = lado*(2**(0.5))
    print("O valor do Perimetro é: ", perimetro)
    print("O valor da Área é: ", area)
    print("O valor da Diagonal é: ", diagonal)

circe(10)