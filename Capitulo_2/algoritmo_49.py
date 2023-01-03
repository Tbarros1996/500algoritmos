# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 49
# Capitulo 2
"""
Entrar com um nome e imprimir:
todo nome:
primeiro caractere:
ultimo caractere:
do primeiro ate o terceiro:
quarto caractere:
todos menos o primeiro:
os dois ultimos:
"""

nome= str(input(print("Entre com o nome: \n")))

todo_nome = nome
primeiro_caractere = todo_nome[0]
print(primeiro_caractere)
ultimo_caractere = todo_nome[len(todo_nome)-1]
print(ultimo_caractere)
do_primeiro_ate_o_terceiro = todo_nome[0:3]
print(do_primeiro_ate_o_terceiro)
quarto_caractere = todo_nome[3]
print(quarto_caractere)
todos_menos_o_primeiro=todo_nome[1:]
print(todos_menos_o_primeiro)
os_dois_ultimos=todo_nome[-3:-1] # deu ruim aqui
print("".join([os_dois_ultimos,todo_nome[-1]])) #famosa gambiarra

