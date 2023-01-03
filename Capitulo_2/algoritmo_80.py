# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 80
# Capitulo 2

"""
Criar um algoritmo que leia o valor de um depósito e o valor da taxa de juros. 
Calcular e imprimir o valor do rendimento e o valor total depois do rendimento.

Criar um algoritmo que leia a quantidade de fitas que uma locadora de vídeo possui e o valor que ela cobra por cada aluguel, mostrando as informações pedidas a
seguir:
* Sabendo que um terço das fitas são alugadas por mês, exiba o
faturamento anual da locadora;


*Quando o cliente atrasa a entrega, é cobrada uma multa de 10% sobre o
valor do aluguel. Sabendo que um décimo das fitas alugadas no mês são
devolvidas com atraso, calcule o valor ganho com multas por mês;

*Sabendo ainda que 2% de fitas se estragam ao longo do ano, e um décimo
do total é comprado para reposição, exiba a quantidade de fitas que a locadora
terá no final do ano.
"""

fitas = int(input(print("Digite a Quantidade de Fitas")))
aluguel = float(input(print("Digite o valor do Aluguel")))

faturamento = (fitas/3) * aluguel *12

print(f"Faturamento anual de {faturamento}")

multas = aluguel * 0.1 * (fitas/3)/10

multas_mensais = print(f"Multas Mensais de {multas}")

quant_final = fitas - (fitas*0.02 + fitas/10)

print(f"Quantidade de Fitas no Fim de Ano {quant_final}")





