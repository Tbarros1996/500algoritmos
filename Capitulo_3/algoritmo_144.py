# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 144
# Capitulo 2

"""
O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de 
acordo com o saldo médio no último ano. Fazer um algoritmo que leia o 
saldo médio de um cliente e calcule o valor do crédito de acordo com a tabela a seguir. 
Imprimir uma mensagem informando o saldo médio e o valor do crédito. 

SALDO MÉDIO PERCENTUAL 
de O a 500 nenhum crédito 
de 501 a 1000 30% do valor do saldo médio 
de 1001 a 3000 40% do valor do saldo médio 
acima de 3001 50% do valor do saldo médio

"""


salario = float(input("Entre com o Salário:  "))


if salario >0 and salario <=500:
    print(f'Você tem 0 de crédito')
elif salario > 500 and salario <=1000:
    print(f'O Valor de credito será {salario*0.3}')
elif salario > 1000 and salario <=3001:
    print(f'O Valor de crédito será {salario*0.4}')
else:
    print(f'O Valor de crédito será de {salario*0.5}')
    
if salario == 0:
    print("Você não possui disponibilidade de crédito")
if salario <0:
    print("Pague o Banco")