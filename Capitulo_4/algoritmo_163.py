# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 163
# Capitulo 4

"""
Algoritmo que repete ciclo de voltas e de abdominais

"""
i = 0
j = 0
voltas = 3
abdominais = 5

for i in range(0,voltas + 1):
    print(f'A volta é a  {i}')
    for j in range(0,abdominais + 1):
        print(f'Ele Fez {j} Abdominais')
    