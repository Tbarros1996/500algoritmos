# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 201
# Capitulo 4

"""
Criar um algoritmo que leia os limites inferior e superior de um intervalo e imprima 
todos os números pares no intervalo aberto e seu somatório. Suponha que os 
dados digitados são para um intervalo crescente

"""
print('Entre com os Limites Inferior e Superior : ')

import numpy as np

li =int(input('LI: '))
ls =int(input('LS: '))
lista = []

for i in range(li+1,ls-1,1):
    if i % 2 == 0:
        print(i)
        lista.append(i)
    else:
        pass
lista_array = np.array(lista)
print(f'A soma é {lista_array.sum()}')

# Nota: Achei mais prático usar o Numpy