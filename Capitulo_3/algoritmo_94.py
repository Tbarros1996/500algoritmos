# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 94 - 95 -96- 97
# Capitulo 2

"""
 Para essas questões usaremos um mesmo algoritimo


Verificar se um número é:


 Questão 94

* Entrar com um número e verificar se ele é múltiplo de 3

 Questão 95
* Verificar se ele é divisivel por 5 ou não

 Questão 96
* Verificar se ele é divisivel por 3 e por 7

 Questão 97
* Verifica se o número é divisivel por 10,05,2 e se não é divisivel por nenhum deles

"""
def alg_94(x):
    if x%3 ==0:
        print("Multiplo de 3")
    else:
        print("Não é multiplo de 3")


def alg_95(x):
    if x%5 == 0:
        print("O número é multiplo de 5")
    else:
        print("Não é multiplo de 5")

def alg_96(x):
    if (x%3 == 0) and (x%7 == 0):
        print("O número é divisivel por 3 e por 7 ao mesmo tempo")
    else:
        print("Não é divisivel por 3 e por 7")

def alg_97(x):
    if (x % 2 == 0) and (x % 10 == 0) and (x % 5 != 0):
      print("É divisivel por 2, 10 mas não por 5")
    elif (x % 2 != 0) and (x % 10 == 0) and (x % 5 == 0):
        print("É divisivel por 5, 10 mas não por 2")
    elif (x % 2 == 0) and (x % 10 != 0) and (x % 5 == 0):
       print("É divisivel por 5, 2 mas não por 10")
    elif (x % 2 == 0) and (x % 10 == 0) and (x % 5 == 0):
       print("É divisivel por todos (2,10,5)")
    else:
        print("Não é divisivel por nenhum dos 3 (2,10,5) ")
    pass



print("Programa de Testes")
print("Deseja executar o programa?")

entrada = str(input(print("[S,N]")))


while entrada == "S" or entrada == "s":
    
    x = float(input(print("Entre com o valor numérico")))
    
    if x == 0 :
        print("Necessário número maior que 0")
    if x <= 0 :
        print("Necessário valores maiores que 0")
    if x  > 0:
        alg_94(x)
        alg_95(x)
        alg_96(x)
        alg_97(x)
    print("Deseja executar o programa novamente? ")
    
    entrada = str(input(print("[S,N]")))



        
       






















