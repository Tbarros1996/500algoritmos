# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 57
# Capitulo 2
"""
Entrar com as notas da PR 1 e PR2 e imprimir a média final:
truncada:
arredondada:

"""

def truncada(pr1 = float, pr2 = float):
    media = (pr1+pr2)/2
    media_truncada = round(((media-0.5)+0.001))
    print(f"A média Foi de {media}, e truncando foi de {media_truncada}")

def arrendondada(pr1 = float, pr2 = float):
    media = (pr1+pr2)/2
    media_arredondada = round((media+0.001))
    print(f"A média Foi de {media}, e arrendondada foi de {media_arredondada}")

truncada(2.3,3.7)
arrendondada(2.3,3.7)

truncada(2.8,2.7)
arrendondada(2.8,2.7)

truncada(7.9,8.1)
arrendondada(7.9,8.1)

truncada(6.9,8.1)
arrendondada(6.9,8.1)