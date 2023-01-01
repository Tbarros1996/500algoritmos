# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 157
# Capitulo 2

"""
Criar um algoritmo que leia uma data (no formato ddmmaaaa) e imprimir se a 
data e valida ou não

"""

dia = int(input("Entre com o dia: "))
mes = int(input("Entre com a mes: "))
ano = int(input("Entre com a ano: "))

print(f'A data é {dia} do {mes} do {ano}')

if dia > 31 or dia <= 0:
    print("A data é invalida")
elif mes >12 or mes <= 0:
    print("O mês é inválido")
elif mes <0:
    print("O ano é inválido")
else:
    print("A data é uma data válida")
      


