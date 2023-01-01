# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 118
# Capitulo 2

"""
Entrar com três números e imprimi-los em ordem crescente (suponha números di -
ferentes).

"""
x = float(input(print("Entre com o X1\a : ")))
y = float(input(print("Entre com o X2\a : ")))
z = float(input(print("Entre com o X3\a : ")))

lista = [x,y,z]
lista_ordenada = sorted(lista)
print(lista_ordenada[0],lista_ordenada[1],lista_ordenada[2])

# Nota:

"""
Nem todos os exercícios desse capitulo eu fiz com estrutura de decisão pois tentei 
fazer da maneira mais simples possível usandas as ferramentas que o python me possibilita

"""