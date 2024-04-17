# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 256
# Capitulo 4

# Palíndromos são palavras (frases também) que são iguais quando lidas de frente
# para trás e de trás para frente, ignorando os espaços.
# AMEOPOEMA AMORA ROMA ATEOPOETA LUZAZUL
# Criar um algoritmo que possa entrar com 15 mensagens e imprimir quantas são
# palíndromos.


lista_1 = []
lista_2 = []
palindromos = 0

for i in range(6):
    registro = str(input(f'Entre Com as Palavra {i}: '))
    lista_1.append(registro)
    lista_2.append(registro[::-1])

for i,j in zip(lista_1,lista_2):
    
    if i == j:
        palindromos += 1

print(f'A quantidade de palindromos foi de {palindromos}')

"""
Nota do programador:

Quando se deseja interar usando duas listas ao mesmo tempo, é preciso usar a função zip(), onde a mesma intera os contadores dentro da listas ao mesmo tempo.

Ver Doc:

https://docs.python.org/pt-br/3/library/functions.html#zip

"""