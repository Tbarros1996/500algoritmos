# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 132
# Capitulo 3

"""
Fazer um algoritmo que possa converter
uma determinada quantia em reais
para uma das seguintes moedas:

f-franco suíço
l-libra esterlina
d- dolar
m - marco alemão
"""

#Modo do Livro

r = float(input("Entre com o valor em reais: "))
x = str(input("Para qual moeda você deseja converter: f-franco; l-libra; d-dolar ; m-marco ? : "))

if x == "f" or x == "F":
    f = float(input("Entre com a cotação do Franco: "))
    cambio_1 = f*r
    print(f'Valor e, R$: {cambio_1}')

elif x == "l" or x == "L":
    l = float(input("Entre com a cotação da Libra: "))
    cambio_2 = l*r
    print(f'Valor de, R$: {cambio_2}' )

if x == "d" or x == "D":
    d = float(input("Entre com a cotação do Dólar: "))
    cambio_3 = d*r
    print(f'Valor de, R$: {cambio_3}')

if x == "m" or x == "M":
    m = float(input("Entre com a cotação do Marco: "))
    cambio_4 = m*r
    print(f'Valor de, R$: {cambio_4}')
    

