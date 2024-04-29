# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 263
# Capitulo 4

"""
Entrar com vários números positivos e imprimir a média dos números digitados.

"""

i = 0
j = 0

while True:
    
    x = int(input('Entre com o Valor Numérico: '))
    
    if x >0:
        
        i += x
        j += 1
    
    print(f'A média atual é de {i/j}')
    
    if x < 0:
        
        break
    
    
    
    
    