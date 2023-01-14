# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 197
# Capitulo 4

"""
Criar um algoritmo que leia um número que servirá para controlar os primeiros 
números ímpares. Deverá ser impressa a soma desses números. Suponha que 
num será maior que zero. 

"""

ls =int(input("Entre com a quantidade de números: "))
k = 0
for contador in range(0,ls*2):
    if contador % 2 != 0:
        k = k + contador

print(f'A soma dos {ls} primeiros impares maiores que 0 é {k}')
    