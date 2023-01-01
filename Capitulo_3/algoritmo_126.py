# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 126
# Capitulo 2


"""
Ler um número e imprimir se ele é iguala 5, a 200, a 400, se está no intervalo en-
tre 500 e 1000, inclusive, ou se ele está fora dos escopos anteriores.

"""

numero = int(input('Entre com um Número'))

if numero == 5:
    print('Igual a 5')
else:
    if numero == 200:
        print('Igual a 200')
    elif numero == 400:
        print('Igual a 400')
    elif numero >= 500 and numero <= 1000:
        print('No intervalo entre 500 e 1000')
    elif numero < 200  or numero > 1000:
        print('Fora de Escopo')