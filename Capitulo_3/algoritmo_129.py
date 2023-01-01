# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 129
# Capitulo 2


"""
Entrar com o salário de uma pessoa e imprimir o desconto do INSS segundo a ta-
bela a seguir:
menor ou igual a R$ 600,00
 isento
 
maior que R$ 600,00 e menor ou igual a R$ 1200,00
 20%
 
maior que R$ 1200,00 e menor ou igual a R$2000,00
 25%
 
maior que R$ 2000,00
 30%

"""


salario = float(input('Entre com o Salário'))


if salario > 2000:
    desconto = salario * 0.3
    print(f'DESCONTO DE R$ {desconto}')
else:
    if salario > 1200 and salario <= 2000:
        desconto = salario * 0.25
        print(f'DESCONTO DE R$ {desconto}')
    elif salario > 600 and salario <= 1200:
        desconto = salario * 0.20
        print(f'DESCONTO DE R$ {desconto}')
    else:
        print('isento')
