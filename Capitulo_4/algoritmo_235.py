# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 235
# Capitulo 4

"""
Entrar com dez números (positivos ou negativos) 
e imprimir o maior e o menor
número da lista.
"""

lista = []

for i in range(0,10,1):
    x = float(input("Entre com o VALOR: "))
    lista.append(x)

print("O maior é:" ,max(lista))
print("O menor é: ", min(lista))