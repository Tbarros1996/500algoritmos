# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 66
# Capitulo 2
"""
Efetuar o cálculo da quantidade de litros de combustível gastos em uma viagem,
sabendo-se que o carro faz 12 km com um litro. Deverão ser fornecidos o tempo
gasto na viagem e a velocidade média.
Utilizar as seguintes fórmulas: distância = tempo x velocidade.
litros usados = distância / 12.
O algoritmo deverá apresentar os valores da velocidade média, tempo gasto
na viagem, distância percorrida e a quantidade de litros utilizados na viagem.

"""

def calc_comb(tempo = float, velocidade = float, rendimento = float):
    distância = tempo*velocidade
    litros = distância/rendimento
    print(f"Foram Gastos: {litros} Litros")
    return litros

x = calc_comb(60,1.2,12)

