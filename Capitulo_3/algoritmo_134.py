# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 134
# Capitulo 2

"""
A confederação brasileira de natação irá promover eliminatórias para o próximo 
mundial Fazer um algoritmo que receba a idade de um nadador e imprimir a sua 
categoria segundo a tabela a seguir: 

Categoria Idade 
InfantilA 5-7anos 
Infantil B 8— 10 anos 
JuvenilA 11 - 13 anos 
Juvenil 14— 17 anos 
Sênior maiores de 18 anos 

"""

idade = int(input("Entre com a idade: "))

if idade < 5:
    print("Não existe catergoria")
elif idade >= 5 and idade <=7:
    print("Catergoria Infantil A")
elif idade >=8 and idade <=9:
    print("Categoria Infantil B") 
elif idade >=10 and idade <=10:
    print("Categoria Infantil B") 
elif idade >=10 and idade <=13:
    print("Categoria Juvenil A") 
elif idade >=14 and idade <=17:
    print("Categoria Juvenil B")
else:
    print("Categoria Senior")     
    

    