# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 148
# Capitulo 3

"""
Criar um algoritmo que leia o destino do passageiro, se a viagem inclui retorno 
(ida e volta) e informar o preço da passagem conforme atabela a seguir.

DESTINO IDA IDA E VOLTA 
Região Norte R$500 00 R$9001 '00 
Região Nordeste R$3501 00 R$650,00 
Região Centro-Oeste R$350,00, R$600f00 
Região Sul R$3001 00 R$5501 00 

"""

# ATENÇÃO: Será usado com o método case match. Funciona a partir da versão 3.10 do Python

destino = print("Defina o Seu Destino: \
                \n 1 - Centro Oeste \
                \n 2 - Sudeste \
                \n 3 - Nordeste \
                \n 4 - Norte\
                \n 5 - Sul ")



#Nota: Sudeste não existe na tabela, mas acabei colocando por acidente;

destino_valor = int(input("[ Destino ]: "))

if destino_valor == 2:
    print("Viagens para o Sudeste ainda não são realizadas pela viação")
elif destino_valor > 5:
    print("Número Incorreto")
    
tipo = print("Defina o Tipo de Viagem: \
                \n 0 - Apenas Ida \
                \n 1 - Ida e Volta ")

tipo_valor = int(input("[ Tipo ]: "))


match destino_valor:
    case 1:
        if tipo_valor == 0:
            print(f'CENTRO OESTE - APENAS IDA - PREÇO: R$ 350,00')
        elif tipo_valor == 1:
            print(f'CENTRO OESTE - IDA e VOLTA - PREÇO: R$ 600,00')
        else:
            print("OPÇÃO INCORRETA")
    case 3:
        if tipo_valor == 0:
            print(f'NORDESTE - APENAS IDA - PREÇO: R$ 350,00')
        elif tipo_valor == 1:
            print(f'NORDESTE - IDA e VOLTA - PREÇO: R$ 650,00')
        else:
            print("OPÇÃO INCORRETA")
    case 4:
        if tipo_valor == 0:
            print(f'NORTE - APENAS IDA - PREÇO: R$ 500,00')
        elif tipo_valor == 1:
            print(f'NORTE - IDA e VOLTA - PREÇO: R$ 900,00')
        else:
            print("OPÇÃO INCORRETA")
    case 5:
        if tipo_valor == 0:
            print(f'SUL - APENAS IDA - PREÇO: R$ 300,00')
        elif tipo_valor == 1:
            print(f'SUL - IDA e VOLTA - PREÇO: R$ 550,00')
        else:
            print("OPÇÃO INCORRETA")       
                

# A idéia é mostrar a utilização do case match juntamente com as condicionais padrão, uma vez que
# só existia uma condição para cada caso