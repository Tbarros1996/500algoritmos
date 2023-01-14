# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 188
# Capitulo 4

"""
Criar um algoritmo que imprima uma tabela de 
conversão de polegadas para centímetros. 
Deseja-se que na tabela conste valores desde 
1 polegada até 20 polegadas inteiras
"""


polegada = []
cm = []

for i in range (0,21):
    conversao = i*2.24
    polegada.append(i)
    cm.append(round(conversao,2))
    print(f'{i}" ------ {cm[i]} Cm')