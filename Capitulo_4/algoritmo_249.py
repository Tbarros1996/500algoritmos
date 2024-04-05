# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 249
# Capitulo 4

"""

Criar um algoritmo que entre com uma palavra e se ,a palavra tiver número ímpar de ca-
racteres, imprima conforme exemplo a seguir, caso contrário, imprima : NAO FACO:
palavra: SONHO
SONHO
SONHO SONHO SONHO
SONHO SONHO SONHO SONHO SONHO

"""

palavra = str(input("Entre com a Palavra: "))
rep = len(palavra)
lista = [x+1 for x in range (len(palavra)) if x % 2 == 0]
 
if rep % 2 != 0:
    for i in range(len(lista)):
        produto = lista[i]
        print((palavra + " " )*produto)
else:
    print("Não Faço")
    