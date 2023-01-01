# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 122
# Capitulo 2


"""
Ler três números e verificar se os três números são possiveis de 
serem lados de um triângulo

"""

lde1 = float(input("Entre com o Primeiro Lado"))
lde2 = float(input("Entre com o Segundo Lado Lado"))
lde3 = float(input("Entre com o Terceiro Lado Lado"))

if (lde1 < lde2 + lde3) and (lde2 < lde3 + lde1) and (lde3 < lde1 + lde2):
    print("Sim , os valores são lados de um triângulo")
else:
    print("Não, os valores não são lados de um triângulo")
    

