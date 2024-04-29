# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 263
# Capitulo 4

"""
Entrar com números enquanto forem positivos e imprimir quantos números fo-
ram digitados.
"""

i = 0

while True:
    
    x = int(input('Entre com o Valor Numérico: '))
    i += 1
    
    if x < 0:
        
        print(f"Foram Registrados {i} Números Positivos")
        break
    
    
    
    
    