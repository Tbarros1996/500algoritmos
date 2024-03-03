# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 234
# Capitulo 4

"""
Entrar com nome e salário bruto de 10 pessoas. 
Imprimir nome e o valor da aliquota do imposto de renda:
salário menor que R$ 600,00
salário > = R$ 600,00 e <R$ 1500,00
salário >= R$ 1500,00
"""

def aliquota(nome=str,salario=float):
    if salario < 600:
        print(f'{nome} está isento de imposto de renda')
    elif  salario>= 600 and salario<1500:
        print(f'{nome} pagará {0.1*salario} de imposto de renda')
    else:
        print(f'{nome} pagará {0.15*salario} de imposto de renda')

for i in range(0,10):
    nome = str(input("Nome da Pessoa: "))
    salario = float(input("Salario: "))
    aliquota(nome,salario)