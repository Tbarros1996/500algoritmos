# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 70
# Capitulo 2
"""
Todo restaurante embora por lei não possa obrigar o cliente a pagar, cobra 10%
para o garçom. Fazer um algoritmo que leia o valor gasto com despesas realizadas 
em um restaurante e imprima o valor total com a gorjeta.

"""

def conta(gasto = float):
    total = gasto*1.1
    print("O valor gasto foi: ", round(total,2))

conta(10.25)