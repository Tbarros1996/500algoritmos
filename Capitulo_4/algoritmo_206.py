# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 206
# Capitulo 4


"""
Criar um algoritmo que leia a quantida de números que se deseja digitar para que possa ser impresso o maior e o menor
número digitados. Não suponha que todos os números lidos serão positivos

"""

quantidade = int(input("Entre com a quantidade de números que deseja digitar : "))
dados = []

for i in range (1 , quantidade+1):
    print(f'Entre com o {i}° Valor')
    x = float(input())
    dados.append(x)

print("Os maiores e menores valores são:")
print(f'Maior valor da sequencia: {max(dados)}')
print(f'Menor valor da sequencia: {min(dados)}')

