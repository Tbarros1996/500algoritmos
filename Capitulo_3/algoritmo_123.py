# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 123
# Capitulo 2


"""
Ler os três lados de um triângulo e verificar qual tipo de triâgulo

"""

lde1 = float(input("Entre com o Primeiro Lado"))
lde2 = float(input("Entre com o Segundo Lado Lado"))
lde3 = float(input("Entre com o Terceiro Lado Lado"))


if (lde1 < lde2 + lde3) and (lde2 < lde3 + lde1) and (lde3 < lde1 + lde2):
    print("Sim , os valores são lados de um triângulo")
    if lde1 == lde2 and lde1 == lde3:
        print("\a O triângulo é equilátero")
    elif lde1 == lde2 or lde1 == lde3 or lde2 == lde3:
        print("O triângulo é isórceles")
    else:
        print("O triaangulo é escaleno")
else:
    print("Não, os valores não são lados de um triângulo")
