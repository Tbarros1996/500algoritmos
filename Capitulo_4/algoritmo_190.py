# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 190
# Capitulo 4

"""
Entrar com um nome, idade e sexo de 20 pessoas. Imprimir o nome se a pessoa for
do sexo masculino e tiver mais de 21 anos.
"""

for contador in range(0,20):
    print("Pessoa", contador + 1)
    nome = str(input("Entre com o nome da Pessoa: "))
    sexo = str(input("Entre com o sexo da Pessoa: "))
    idade =int(input("Entre com a idade da Pessoa: "))
    if (idade >20 and sexo == "m") or (idade >20 and sexo == "m"):
        print(f'Nome: {nome}, Idade: {idade}')
    elif idade <=20 or sexo == "f" or sexo == "F" :
        pass
    
    
