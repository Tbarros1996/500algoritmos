# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 200
# Capitulo 4

"""
Criar um algoritmo que leia os limites inferior e superior de um intervalo e o 
número cujos múltiplos se deseja que sejam impressos no intervalo aberto. 
Suponha que os dados digitados são para um intervalo crescente
"""
print('Entre com os Limites Inferior e Superior e o número que deseja os múltiplos : ')

li =int(input('LI: '))
ls =int(input('LS: '))
mult =int(input('Numero: '))

for i in range(li+1,ls+1,1):
    if i % mult==0:
        print(i)
    else:
        pass