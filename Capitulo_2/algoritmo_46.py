# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 46
# Capitulo 2
"""
Fazer um algoritmo que possa entrar com o saldo de uma aplicação e imprima o
novo saldo, considerando o reajuste de 1%.
"""

salario = float(input(print("Entre com o Salario")))
reajuste_percentual = float(input(print("Entre com o valor de reajuste %")))

reajuste = salario*(1+(reajuste_percentual/100))

print("O novo salario é de : ", reajuste)
