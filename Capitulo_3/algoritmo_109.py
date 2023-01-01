# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 109
# Capitulo 2


#Obs: Nessa eu também não entendi, mas ele considera o comprimento do maior nome
# Logo, aquele que tiver maior comprimento vai na frente

"""
Criar um algoritmo que entre com dois nomes e imprimi-los em ordem alfabética.
"""
import timeit

def nome_alfa(nome,sobrenome):
    if len(nome)>len(sobrenome):
        print(nome," ",sobrenome)
    elif len(nome) == len(sobrenome):
        print(nome," ",sobrenome)
    else:
        print(sobrenome," ", nome)
        
nome = str(input(print("Entre com o Nome\a : ")))
sobrenome = str(input(print("Entre com o Sobrenome\a : ")))
nome_alfa(nome,sobrenome)
print("Tempo de Execução",":",timeit.timeit('char in text', setup='text = "sample string"; char = "g"'))