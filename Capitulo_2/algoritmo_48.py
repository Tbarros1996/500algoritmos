# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 48
# Capitulo 2
"""
Antes de o racionamento de energia ser decretado, quase ninguém falava em
quilowatts; mas, agora, todos incorporaram essa palavra em seu vocabulário.

Sabendo-se que 100 quilowatts de energia custa um sétimo do salário mínimo,

fazer um algoritmo que receba o valor do salário mínimo e a quantidade de 
quilowatts gasta por uma residência e calcule. 

Imprima:
o valor em reais de cada quilowatt
m o valor em reais a ser pago
o novo valor a ser pago por essa residência com um desconto de 10%

"""

salario = float(input(print("Entre com Seu Salário: \n")))
watts = float(input(print("Quantos KW foram gastos? : \n")))

unidade_kw = salario/700

custo = watts * unidade_kw

custo_desconto_90 = custo*(1-0.1)

print("O Total Foi de: ", custo, "E com desconto foi de: ", custo_desconto_90)