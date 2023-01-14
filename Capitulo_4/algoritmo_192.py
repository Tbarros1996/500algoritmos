# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 192
# Capitulo 4

"""
Criar um algoritmo que leia um número que será o limite superior de um intervalo
e imprimir todos os números ímpares menores do que esse número.

"""
ls =int(input("Entre com a Limite Superior: "))

i = 0

for contador in range(0,ls+1):
    if contador % 2 != 0 :
        print(contador)
        i += 1
    else:
        pass
    
print(f'Existem {i} números impares entre 0 e {ls}')    
    
