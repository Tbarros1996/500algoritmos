# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 73
# Capitulo 2


"""
Cria um algoritmo qe receba um numero real, calcular
imprimir:

° A parte interira do número
° A parte fracionaria do número
° O número arrendondado

"""

# Dica: Existe uma função no módulo math que retorna a parte fracionária e inteira de um valor numérico - math.modf()

import math as mt

numero = float(input("Entre com o valor: "))
real = mt.modf(numero)
print(f'A parte fracionária é {round(real[0],3)}, e a parte inteira é {round(real[1],0)}')
