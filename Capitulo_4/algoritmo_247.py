# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 247
# Capitulo 4

"""

Num campeonato europeu de volleyball, se inscreveram 30 países. Sabendo-se
que na lista oficial de cada país consta, além de outros dados, peso e idade de 12
jogadores criar um algoritmo que apresente as seguintes informações
m o peso médio e a idade média de cada um dos times;
m o peso medio e a idade media de todos os participantes

"""


# Para esse algoritmo, farei diferente: Definirei a lista de 12 Atletas e vamos # percorrer a lista com o laço de repetição


pais = ["Brasil","Alemanha","Argentina","Holanda","Alemanha","Italia",
        "França","Inglaterra","Brasil","EUA","EUA","Colombia"]

peso = [78.5,77.6,81.5,78.9,80.2,77.5,78.5,77.6,81.5,78.9,80.2,77.5]

idade = [28,27,28,26,27,25,28,27,28,26,27,25]

# Vamos usar um set para criar uma coleção de valores não repetidos, e 
# ordena-los por ordem alfabética

# Dica: Podemos associar uma Key em um dict a uma list ex: {Brasil: [122,23]}

lista_peso = {}
lista_idade = {}
lista_pais = sorted(list(set(pais)))

banco_peso = {chave : [] for chave in lista_pais}
banco_idade = {chave : [] for chave in lista_pais}
    
for j in range(len(pais)):
    
    pais_loop = pais[j]
    peso_loop = peso[j]
    idade_loop = idade[j]
    
    if pais_loop in banco_peso:
        banco_peso[pais_loop].append(peso_loop)
        banco_idade[pais_loop].append(idade_loop)

for k in banco_peso:
    lista = banco_peso.get(k)
    media = sum(lista)/len(lista)
    lista2 = banco_idade.get(k)
    media2 = sum(lista2)/len(lista2)
    print(f'País: {k}, Peso Média {media},  Idade Média {media2}')
    
print(f'Total de Participantes {len(pais)}') 
print(f'Peso Médio Geral: {sum(peso)/len(peso)}') 
print(f'Idade Média Total {sum(idade)/len(idade)}')      