# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 212
# Capitulo 4

"""
Entrar com 20 números e imprimir a soma dos números cujo os quadrados são menores que 225

"""
soma = 0

for i in range(1,21):
    if i**2 < 225:
        soma += i
    else:
        pass
print(soma)