# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 106
# Capitulo 2


"""
Entrar com um nome e imprimi-lo se o primeiro caractere for a letra A (considerar
letra minúscula ou maiúscula).

"""
a = ["A","a"]

nome = str(input(print("Entre com um Nome")))

nome_lista = list(nome)

if nome_lista[0] == a[0] or nome_lista[0] == a[1] :
    print(nome)
else:
    pass