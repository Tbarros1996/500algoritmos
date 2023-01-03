# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 147
# Capitulo 3

"""
Criar um algoritmo que informe a quantidade total de calorias de uma refeição a 
partir da escolha do usuário 'que deverá informar o prato, a sobremesa e bebida 
(veja a tabela a seguir). 
PRATO SOBREMESA BEBIDA 
Vegetariano 180cal Abacaxi 75cal Chá 20caI 
Peixe 230cal Sorvete diet 11 Oca! Suco de laranja 70cal 
Frango 250ca! Mousse diet 1 7Oca! Suco de melão 1 OOca! 
Carne 350ca! Mousse chocolate 200cal Refrigerante diet 65cal

"""

#Opcional - Importação do Módulo Pandas Para Visualização

import pandas as pd

def prato(x = int):
    if x  == 1:
        return 180
    elif x == 2:
        return 230
    elif x == 3:
        return 250
    elif x == 4:
        return 350
    else:
        KeyError

def sobremesa(y = int):
    if y  == 1:
        return 75
    elif y == 2:
        return 110
    elif y == 3:
        return 170
    elif y == 4:
        return 200
    else:
        KeyError
        
def bebida(z = int):
    if z  == 1:
        return 20
    elif z == 2:
        return 70
    elif z == 3:
        return 100
    elif z == 4:
        return 65
    else:
        KeyError
    
print("Bom dia. Entre com a sua escolha no cardápio \n")

tabela_precos = pd.DataFrame({"Prato":["1-Vegetariano","2-Peixe","3-Frango","4-Carne"],\
    "Sobremesa":["1-Abacaxi","2-Sorvete Diet","3-Mousse Diet","4-Mousse Chocolate"],\
    "Bebida":["1-Chá","2-Suco de Laranja","3-Suco de Limão","4-Refrigerante Diet"]})

print(tabela_precos)

x = int(input("[Prato]: "))
y = int(input("[Sobremesa]: "))
z = int(input("[Bebida:]: "))

#Prato

if x == 1:
    a = "Vegetariano"
elif x == 2:
    a = "Peixe"
elif x == 3:
    a = "Frango"
elif x == 4:
    a = "Carne"
else:
    print("Prato Inexiste")
    KeyError

#Sobremesa

if y == 1:
    b = "Abacaxi"
elif y == 2:
    b = "Sorvete Diet"
elif y == 3:
    b = "Mousse Diet"
elif y == 4:
    b = "Mousse Chocolate"
else:
    print("Prato Inexiste")
    KeyError

#Bebida

if z == 1:
    c = "Chá"
elif z == 2:
    c = "Suco de Laranja"
elif x == 3:
    c = "Suco de Limão"
elif z == 4:
    c = "Refrigerante Diet"
else:
    print("Prato Inexiste")
    KeyError

calorias  = prato(x) + sobremesa(y) + bebida(z)

print(f'Você escolheu como prato o/a {a}, e para sobremesa o/a {b}, e por fim como bebida um {c}. \
    \n Seu prato terá {calorias} Calorias ao todo. Boa refeição.')