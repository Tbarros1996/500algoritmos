# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 98
# Capitulo 2

"""
A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários es -
tatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
bruto Fazer um algoritmo que permita entrar com o salário bruto e o valor da
prestação e informar se o empréstimo pode ou não ser concedido.

"""

def emprestimo(salario=float, percentual = float):
    if salario * (percentual/100) > 0.3:
        print("Emprestimo Negado")
    else:
        print("Emprestimo concedido")

salario = float (input(print("Entre com o Número : ")))
percentual = float (input(print("Entre com o Número : ")))
emprestimo(salario,percentual)
