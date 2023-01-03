# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 135
# Capitulo 3

"""
Criar um algoritmo que leia a idade de uma pessoa e informara sua classe eleitoral: 
m não-eleitor (abaixo de 16 anos) 
m eleitor obrigatório (entre 18 e 65 anos) 
eleitor facultativo (entre 16 e 18 anos e maior de 65 anos)  

"""

idade = int(input("Entre com a idade: "))

if idade < 16:
    print("Não pode votar")
elif idade >= 18 and idade <=65:
    print("Voto Obrigatório")
elif (idade >=16 and idade <=17) or (idade > 65):
    print("Voto facultativo") 
  
    

    