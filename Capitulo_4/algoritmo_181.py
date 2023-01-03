# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 181
# Capitulo 4

"""
Criar um algoritmo que imprima todos os 
numeros de 1 ate 100 e a soma deles 

"""
y=0

for x in range(0,101,1):
    y = y + x
    print(f'O número é {x}')
    print(f'A soma é {y}')