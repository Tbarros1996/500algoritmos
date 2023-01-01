# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 133
# Capitulo 2

"""
Segundo uma tabela médica
, o peso ideal está relacionado
com a altura e o sexo da pessoa.

Fazer uma algoritmo que revebe a altura e 
o sexo da pessa e imprima  o peso ideal com base nas fórmulas:

para homens (72.7*H) -58
para mulheres (62.1*H) - 44.7
"""

s = str(input("Você é Homem ou Mulher?: "))
a = float(input("Entre com sua altura em Metros: "))

if s=="h" or s=="H":
    peso_1 = 72.7*a -58
    print(f'Seu peso ideal é {peso_1}')
elif s=="M" or s=="m":
    peso_2 = 61.1*a - 44.7
    print(f'Seu peso ideal é {peso_2}')

