# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 124
# Capitulo 2


"""
Ler três números, os possíveis lados de um triângulo e imprimir a classificação
com base nos seus ângulos

"""

lde1 = float(input("Entre com o Primeiro Lado"))

lde2 = float(input("Entre com o Segundo Lado Lado"))

lde3 = float(input("Entre com o Terceiro Lado Lado"))


if (lde1 < lde2 + lde3) and (lde2 < lde3 + lde1) and (lde3 < lde1 + lde2):
    
    print("Sim , os valores são lados de um triângulo")
    
    if lde1 > lde2 and lde1 > lde3:
        
        maior = lde1 ** 2
        
        lados = lde3 ** 2 + lde2 ** 2
        
        if maior == lados:
            
            print("Retângulo Retângulo")
            
        elif maior > lados:
            
            print('Triâgulo Obtusângulo')
            
        else:
            
            print('Triângulo Acutângulo') 
    else:
        
        if lde2 > lde3:
            
            maior = lde2 ** 2
            
            lados = lde3 ** 2 + lde1 ** 2
            
        else:
            maior = lde3 ** 2
            
            lados = lde1 ** 2 + lde2 ** 2
            
        if maior == lados:
            
            print("Retângulo Retângulo")
            
        elif maior > lados:
            
            print('Triâgulo Obtusângulo')
            
        else:
            print('Triângulo Acutângulo') 
            
if  ((lde1 < lde2 + lde3) and (lde2 < lde3 + lde1) and (lde3 < lde1 + lde2)) == False:
    
    print('Não é possivel ter os lados de um triângulo')

    
             

    
  
