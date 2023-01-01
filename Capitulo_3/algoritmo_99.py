
# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 99
# Capitulo 2

"""
Ler um número inteiro de 3 algarismos e 
verificar se o algarismo da casa das centenas é par o impár

"""
import math as mt
valor = float(input(print("Entre com o valor numérico")))
valor_centena = int(mt.trunc(valor/100))

if (valor_centena % 2) == 0:
    print("O primeiro Valor é Par")
else:
    print("O Primeiro Valor é ímpar")
