# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 209
# Capitulo 4


"""
A série de RICCI difere da série de FIBONACCI porque os dois primeiros termos
são fornecidos pelo usuário. Os demais termos são gerados da mesma forma que
a série de FIBONACCI. Criar um algoritmo que imprima os n primeiros termos da
série de RICCI e a soma dos termos impressos, sabendo-se que para existir esta série
serão necessários pelo menos três termos.

"""

print("Programa da Série de Ricci")

primeiro_termo = int(input('Entre com o primeiro termo da série: '))
segundo_termo = int(input('Entre com o segundo termo da série: '))
terceiro_termo = int(input('Entre com o terceiro termo da série: '))
n = int(input('Entre com a quantidade de termos que deseja que sejam adicionados a série: '))
ricci = [primeiro_termo,segundo_termo,terceiro_termo]

i = 2

if len(ricci) >= 3: 
    
    while i < n:
        soma = ricci[i] + ricci[i - 1]
        ricci.append(soma)
        i += 1
    print(f'A sequencia de ricci para os {n}° Termos é: ')
    print(ricci)
    
else:
    print("Necessário pelo menos 3 termos")


