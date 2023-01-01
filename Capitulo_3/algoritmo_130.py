# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 130
# Capitulo 2


"""
Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%.
Entrar com o valor do produto e imprimir o valor da venda.

"""


valor_produto = float(input('Entre com o Valor do produto'))


if valor_produto <  20:
    lucro = valor_produto * 1.45
    print(f'venda de R$ {lucro}')
else:
    lucro = valor_produto * 1.3
    print(f'venda de R$ {lucro}')
    
