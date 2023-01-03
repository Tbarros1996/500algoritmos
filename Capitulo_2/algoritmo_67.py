# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 67
# Capitulo 2
"""
Efetuar o cálculo do valor de uma prestação em atraso, utilizando a fórmula:
prestação = valor + (valor*(taxa/100)*tempo).
"""

def prestacao(valor=float,tempo=float,taxa=float):
    prestacao_valor = valor + (valor*(taxa/100))*100
    print(f"E a prestação é  de {prestacao_valor}")
    return prestacao_valor

prestacao(10,10,40)