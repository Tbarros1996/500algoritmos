# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 121


"""
Efetuar a leitura de cinco números inteiros diferentes e identificar o maior e o me-
nor valor.

"""

a = int(input("Entre com X1: "))
b = int(input("Entre com X2: "))
c = int(input("Entre com X3: "))
d = int(input("Entre com X4: "))
e = int(input("Entre com X5: "))

def menor(a,b,c,d,e):
    lista = [a,b,c,d,e]
    lista_ordenada = sorted(lista)
    menor = lista_ordenada[0]
    print("\a")
    print('O menor é', menor)
    print("O maior é", lista[len(lista_ordenada)-1])

menor(a,b,c,d,e)
