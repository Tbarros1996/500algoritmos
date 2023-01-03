# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 138
# Capitulo 3

"""
Ler um número inteiro entre 1 e 12 e escrever o mês correspondente. Caso o 
usuário digite um número fora desse intervalo, deverá aparecer uma mensagem 
informando que não existe mês com este número. 

"""
#Exemplo de aplicação do condicional Match Case. Esse algorítimo só vai funcionar
#a partir da versão 3.10 

def mes(numero = int):
    match numero:
        case 1:
            print("Janeiro")
        case 2:
            print ("Fevereiro")
        case 3:
            print("Março")
        case 4:
            print("Abril")
        case 5:
            print("Maio")
        case 6:
            print("Junho")
        case 7:
            print("Julho")
        case 8:
            print("Agosto")
        case 9:
            print("Setembro")
        case 10:
            print("Outubro")
        case 11:
            print("Novembro")
        case 12:
            print("Dezembro")
    if numero > 12:
        print("Mês não Existente")
        
numero = int(input("Entre com valor de 1 a 12: "))
mes(numero)