# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 105
# Capitulo 2


"""
Entrar com a idade de uma pessoa e informar:

* se é maior de idade
* se é menor de idade
* se é maior de 65 anos

"""
idade = int(input('Entre com a Idade: \a'))

if idade < 18:
    print('Menor de Idade')
else:
    if idade > 65:
        print('Idoso')
    else:
        print('Maior de Idade')