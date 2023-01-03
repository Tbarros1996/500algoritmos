# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 140
# Capitulo 3


"""
Um restaurante faz uma promoção semanal de descontos para clientes de acordo 
com as iniciais do nome da pessoa. Criar um algoritmo que leia o primeiro nome 
do cliente, o valor de sua conta e se o nome iniciar com as letras A, D, M ou S, dar 
um desconto de 30%. Para o cliente cujo nome não se inicia por nenhuma dessas 
letras, exibir a mensagem "Que pena. Nesta semana o desconto não é para seu 
nome; mas continue nos prestigiando que sua vez chegara"

"""

nome = list(str(input("Entre com seu nome: ")))
conta = float(input("Entre com a conta: "))
desconto = list(["A","a","D","d","M","m","S","s"])
if  nome[0] in desconto:
    print(f'Você tem um desconto de {round(conta*0.7,2)}')
else:
    print("Que pena. Nesta semana o desconto não é para seu \
nome; mas continue nos prestigiando que sua vez chegara")

