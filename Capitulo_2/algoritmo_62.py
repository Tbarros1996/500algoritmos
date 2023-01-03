# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 62
# Capitulo 2
"""

Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas
vendas oferecendo desconto. Faça um algoritmo que possa entrar com o valor de
um produto e imprima o novo valor tendo em vista que o desconto foi de 9%.

Extra: Com documentação

"""

def desconto(preco = float, percentual = float):
    """
    \a
    \a
    Uma funcao que calcula um desconto de um preço de Produto

    Argumentos:
        preco:  [Preco do Produto]. Padrao float.
        percentual: [Valor Percentual do Desconto]. Padrao float.
    
    """
    desconto = preco * (1-(percentual/100))
    print(f"O desconto fez o preço reduzir para {desconto} ")

help(desconto)
desconto(20,9)