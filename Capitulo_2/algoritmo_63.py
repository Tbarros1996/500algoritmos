# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 63
# Capitulo 2
"""

Criar um algoritmo que efetue o cálculo do salário líquido de um professor.
Os dados fornecidos serão: valor da hora aula, número de aulas dadas no mês e percentual de desconto do INSS

"""
na = float(input("Entre com as horas trabalhadas: "))
vha = float(input("Entre com as hora aula: "))
pd= float(input("Entre com as horas trabalhadas: "))

sb = na*vha
td = (pd/100)*sb
sl = sb-td
print(f'Salário Líquido de R${sl}')