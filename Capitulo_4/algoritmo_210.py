# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 210
# Capitulo 4


"""
série de FETUCCINE é gerada da seguinte forma: os dois primeiros termos são
fornecidos pelo usuário; a partir dai., os termos são gerados com a soma ou subtração
dos dois termos anteriores, ou seja:

    a(i) = a(i-1) + a(i-2) para impar
    
    a(i) = a(i-1) - a(i-2) para par

"""

print("Programa da Série de Fetuccine")

primeiro_termo = int(input('Entre com o primeiro termo da série: '))
segundo_termo = int(input('Entre com o segundo termo da série: '))
termoS = int(input('Entre com o número de termos da sequencia '))

i = 1
n = 0
fetuccine = [primeiro_termo, segundo_termo]

while n < len(fetuccine):
    
    if i % 2 == 0:
        soma = fetuccine[i] + fetuccine[i - 1]
        fetuccine.append(soma)
        n += 1
        i += 1
    else:
        subtracao = fetuccine[i] + fetuccine[i - 1]
        fetuccine.append(subtracao)
        n += 1
        i += 1

print(f'A sequencia de Fetuccine é f{fetuccine}')


