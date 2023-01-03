# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 78
# Capitulo 2


"""
Dado um polígono convexo de n lados, podemos calcular o número de diagonais 
diferentes (nd) desse polígono pela fórmula : nd = n (n —3)! 2. 
Fazer um algoritmo que leia quantos lados tem o polígono, calcule e escreva o número de diagonais diferentes (nd) do mesmo

"""
a = int(input('Entre com o número de lados: '))
dia = a*((a-3)/2)
print(f'E o poligono tem {int(dia)} diagonais')