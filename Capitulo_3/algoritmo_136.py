# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 136
# Capitulo 3

"""
Depois da liberação do governo para as mensalidades dos planos de saúde, as 
pessoas começaram a fazer pesquisas para descobrir um bom plano, não muito 
caro. Um vendedor de um plano de saúde apresentou a tabela a seguir. Criar um 
algoritmo que entre com o nome e a idade de uma pessoa e imprimir o nome e o 
valor que ela deverá pagar. 

Até l0 anos R$ 30 00 
acima de 10 até 29 anos - R$ 60,00 
acima de 29 até 45 anos - R$ 120,00 
acima de 45 até 59 anos - R$ 150,00 
acima de 59 até 65 anos - R$ 250,00 
maior que 65 anos - R$ 400,00 

"""
nome = str(input("Digite seu Nome: "))
idade = int(input("Digite sua Idade: "))

if idade <= 10:
    print(f'{nome}, você receberá R$ 30,00')
elif idade >10 and idade <=29:
    print(f'{nome}, você pagará R$ 60,00')
elif idade >29 and idade <=45:
    print(f'{nome}, você pagará R$ 120,00')
elif idade >45 and idade <=59:
    print(f'{nome}, você pagará R$ 150,00')
elif idade >59 and idade <=65:
    print(f'{nome}, você pagará R$ 250,00')
else:
    print(f'{nome}, você pagará R$ 400,00')   

    