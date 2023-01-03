# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 60
# Capitulo 2
"""
Entrar com a razão de uma PA e o valor do 1° termo. 
Calcular, imprimir o 10 termo da serie.
"""

def pa10(termo = float, razao = float):
    enc = termo + 9*razao
    print(f"O décimo termo será {enc}")
pa10(1,1)