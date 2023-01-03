# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 75
# Capitulo 2


"""
Criar um algoritmo que leia o peso de uma pessoa, só a parte inteira, calcular e 
imprimir: 
° o peso da pessoa em gramas 
° novo peso em gramas se a pessoa engordar 12%

"""

peso = int(input("Entre com a parte inteira do peso em kg: "))
novo_peso = peso*1000*1.12
print(f'Peso em Gramas {round(peso)},2')
print(f'Novo peso {round(novo_peso,2)}g aumentado em 12%')
