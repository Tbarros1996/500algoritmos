# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 61
# Capitulo 2
"""

Entrar com a razão de uma PG e o valor do 1 2 termo. 
Calcular e imprimir o 5 termo da série.

"""

def pg5(termo = float, razao = float):
    enc = termo * razao**4
    print(f"O quinto termo será {enc}")
pg5(1,1)