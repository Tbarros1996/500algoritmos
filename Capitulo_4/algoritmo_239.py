# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 239
# Capitulo 4

"""
Implementar um algoritmo para calcular o 
valor de eX O valor de X devera ser digitado. 
O valor de eX será calculado pela soma dos 1
0 primeiros termos da serie a
seguir

Comentários:

O que temos é um problema de expansão da série de taylor para função
exponencial.

Temos então que expandir a função para determinar e quando elevando a x

Para esse algoritmo, faremos a comparação do valor aproximado
com o valor verdeiro e calcular a diferença percentual

A expação vai de n=0 até n
"""

import math as mt


valor_potencia = float(input('Entre com o valor da potencia: '))
interacoes = int(input('Entre com o número de termos da expansão: '))

exponencial = 0

for i in range(0,interacoes):
    exponencial += round((valor_potencia**i)/mt.factorial(i),2)
    erro = (1-exponencial/mt.exp(valor_potencia))*100
    print(f'Valor Verdadeiro:  {round(mt.exp(valor_potencia),2)} Valor Aproximado {exponencial} Erro {erro}')
    



