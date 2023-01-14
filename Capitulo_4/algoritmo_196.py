# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 196
# Capitulo 4

"""
Criar um algoritmo que leia um número (num) e imprima a soma dos números 
múltiplos dé 5 no intervalo aberto entre 1 e num. Suponha que num será maior 
que zero. 

"""

ls =int(input("Entre com a Limite Superior: "))
k = 0
for contador in range(1,ls):
    if contador % 5 == 0:
        k = k + contador

print(f'A soma dos multiplos de 5 de 1 a {ls} é {k}')
    