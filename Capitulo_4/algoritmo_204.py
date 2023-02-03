# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 204
# Capitulo 4

"""
Criar um algoritmo que leia um número da entrada (num), leia n números inteiros 
da entrada e imprima o maior deles. Suponha que todos os números lidos serão 
positivos. 

"""


print('Entre com o número: ')

num = int(input('Número: '))
lista = []

for i in range(0,num):
    print('Entre com o número: ')
    x = int(input('Número: '))
    lista.append(x)
    
print(f'E o maior valor dessa série de valores é {max(lista)}')