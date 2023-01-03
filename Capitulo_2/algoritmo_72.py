# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 72
# Capitulo 2
"""
Criar um algoritmo que leia o valor de um depósito e o valor da taxa de juros. 
Calcular e imprimir o valor do rendimento e o valor total depois do rendimento.
"""

deposito = float(input(print("Qual o valor do Depósito?:  ")))
taxa = float(input(print("Qual o valor da taxa de juros?:   ")))
juros = deposito * (taxa/100)
montante = juros + deposito
print(f"O valor do Montante Foi de {montante}")
