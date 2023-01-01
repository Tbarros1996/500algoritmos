# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 107/108
# Capitulo 2


"""
Entrar com o nome de uma pessoa e so imprimi-lo se o 
prenome for JOSE

"""

nome = str(input(print("Entre com um Nome")))
nome_lista = list(nome)
prenome = nome_lista[0:4]
primeira = ["J","j"]
segunda = ["O","o"]
terceira = ["S","s"]
quarte = ["E","e","É","é"]

if prenome[0] == primeira and prenome[1] == terceira and prenome[2] == terceira and prenome[3]==quarte:
    print("nome")
else:
    pass

