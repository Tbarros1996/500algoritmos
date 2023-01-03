# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 74
# Capitulo 2


"""
Para vários tributos, a base de cálculo é o salário mínimo. Fazer um algoritmo que 
leia o valor do salário mínimo e o valor do salário de uma pessoa. Calcular e impri -
mir quantos salários mínimos ela ganha. 

"""

# Dica: Existe uma função no módulo math que retorna a parte fracionária e inteira de um valor numérico - math.modf()

import math as mt

salmin = float(input('Entre com o salário minimo: '))
salpe = float(input('Entre com o salário da pessoa: '))
num = salpe/salmin

print(f'A pessoa ganha {num}, salários minimos')