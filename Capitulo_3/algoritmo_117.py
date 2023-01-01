# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 117
# Capitulo 2

"""
Entrar com três numeros e armazenar o maior numero na variavel de nome maior
(suponha números diferentes)


"""
x = float(input(print("Entre com o X1\a : ")))
y = float(input(print("Entre com o X2\a : ")))
z = float(input(print("Entre com o X3\a : ")))


def teste(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    elif z>y and z>x:
        return z
    if x==y==z:
        return 0

def atribuicao(maior):
    if maior != 0:
        print(f'O maior número é {maior}')
    else:
        print('O número é zero')
        
maior = teste(x,y,z)
atribuicao(maior)