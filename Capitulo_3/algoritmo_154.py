# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 154
# Capitulo 2

"""
A polícia rodoviaria resolveu cumprir a lei e cobrar dos mo
toristas o DUT. Sabendo o mês em que o emplacamento do carro
deve ser renovado é determinado pelo último número 
da placa do mesmo, crie um algoritmo que 
a partir da placa do carro, forme o ês em que o emplacamento deve ser 
renovado.

"""

# ATENÇÃO: Será usado com o método case match. Funciona a partir da versão 3.10 do Python


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
        case 0:
            print("Outubro")
    if numero > 9:
        print("Placa Inválida")
        
numero = str(input("Entre com a placa:  \a"))
numero = int(numero[-1])
mes(numero)


