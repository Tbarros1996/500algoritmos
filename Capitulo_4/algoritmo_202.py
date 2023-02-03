# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 202
# Capitulo 4

"""
Criar um algoritmo que leia um número (num) da entrada e imprima os múltiplos 
de 3 e 5 ao mesmo tempo no intervalo de 1 a num. Exemplo: 

"""
print('Entre com o número: ')

num = int(input('Número: '))

for i in range(1, num+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    else:
        pass