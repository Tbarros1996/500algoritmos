# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 203
# Capitulo 4

"""
Criar um algoritmo que leia um número (num) da entrada. Em seguida, ler n
números da entrada e imprimir o triplo de cada um. Exemplo: 

"""
print('Entre com o número: ')

num = int(input('Número: '))

for i in range(0,num):
    print('Entre com o número: ')
    x = int(input('Número: '))
    print(f'{i} - {x**3}')