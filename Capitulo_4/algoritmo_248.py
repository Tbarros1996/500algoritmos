# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 248
# Capitulo 4

"""

Criar um algoritmo que entre com uma palavra e imprima conforme exemplo a
seguir:
palavra: SONHO
SONHO
SONHO SONHO
SONHO SONHO SONHO
SONHO SONHO SONHO SONHO
SONHO SONHO SONHO SONHO SONHO

"""

palavra = str(input("Entre com a Palavra: "))
rep = int(input("Entre com a Quantidade: "))
for i in range(rep):
    print((palavra + " ")*i)