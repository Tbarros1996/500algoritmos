# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 198
# Capitulo 4

"""
Criar um algoritmo que leia os limites inferior e superior de um intervalo e 
imprima todos os números naturais no intervalo fechado. Suponha que os dados digitados são para um intervalo crescente. 

"""
print('Entre com os Limites Inferior e Superior: ')
li =int(input('LI: '))
ls =int(input('LS: '))

for i in range(li,ls+1,1):
    print(i)