# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 149
# Capitulo 3

"""
Um comercieante calcula o valor da venda, tendo em vista a tabela
a seguir

VALOR DA COMPRA VALOR DA VENDA 
Valor < R$ 10,00 lucro de 70% 
R$10,00 ~ valor < R$ 30,00 lucro de 50% 
R$30, 00 ::~, valor < R$ 50,00 lucro de 40% 
Valor > R$50,00 lucro de 30%

Criar o algoritmo que possa entrar com nome do produto e valor da compra e im
primir o nome do produto e o valor da venda. 

"""


nome_produto = str(input("Digite o nome do Produto \n [Nome]: "))
valor = float(input("Entre com o valor da compra \n [Valor]: "))
if valor < 10:
    print(f'O Valor de {nome_produto} é {valor*1.7}')
elif valor >= 10 and valor <30:
    print(f'O Valor de {nome_produto} é {valor*1.5}')
elif valor >= 30 and valor <50:
    print(f'O Valor de {nome_produto} é {valor*1.4}')
else:
    print(f'O Valor de {nome_produto} é {valor*1.3}')