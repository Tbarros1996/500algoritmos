# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 145
# Capitulo 2

"""
A biblioteca de uma universidade deseja fazer um algoritmo que leia o nome do 
livro que será emprestado, o tipo de usuário (professor ou aluno) e possa 
imprimir um recibo conforme mostrado a seguir. Considerar que o professor tem dez 
dias para devolver o livro e o aluno só três dias. 
Nome do livro 
Tipo de usuário: 
Total de Dias:

"""


nomedolivro = str(input("Entre com o nome do Livro: "))
tipouser = str(input("Entre com o tipo de usuario do Livro [Professor ou Aluno]: "))

if tipouser == "Professor" or tipouser == "professor" :
    print(f'Nome do Livro : {nomedolivro} \n Tipo de Usuario: {tipouser} \n Total de dias: 10 ')
elif tipouser == "Aluno" or tipouser == "aluno":
    print(f'Nome do Livro : {nomedolivro} \n Tipo de Usuario: {tipouser} \n Total de dias: 3 ')
else:
    print("Usuario Desconhecido")    