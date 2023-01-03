# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 76
# Capitulo 2


"""
Criar um algoritmo que leia um 
número entre O e 60 e imprimir o 
seu sucessor, sabendo que o sucessor de 60 é 0. 
Não pode ser utilizado nenhum comando 
de seleção e nem de repetição. 

"""
numero = int(input('Entre com o número: '))
print(f'sucessor: {(numero + 1)%61}')

# Esse algoritmo apesar da simplicidade, ele pode gerar estranheza. Basicamente, todo o resto de divisão
# por 61 será o próprio número até 60 quando a soma retorna 61%61 e o retorno será zero