# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 151
# Capitulo 2

"""
Um endocrinologista deseja controlar a saúde de seus pacientes e, para isso, se 
utiliza do Índice de Massa Corporal (IMC). Sabendo-se que o lMCé calculado através da seguinte fórmula:


IMC = peso / (altura) ^ 2


Onde: 
-peso é dado em Kg 
- altura é dada em metros 

Criar um algoritmo que apresente o nome do paciente e sua faixa de risco, baseando-se na seguinte tabela:

IMC FAIXA DE RISCO 
abaixo de 20 abaixo do peso 
a partir de 20 até 25 normal 
acima de 25 até 30 excesso de peso 
acima de 30 até 35 obesidade 
acime de 35 obesidade mórbida

"""

nome = str(input("Entre como o nome do paciente: "))
peso = float(input("Entre como o peso do paciente: em KG "))
altura = float(input("Entre como a atura do paciente: em Metros "))

imc = peso/(altura**2)
print(f'Imc de {imc}')

if imc < 20:
    print(f'{nome} está abaixo do peso')
elif imc >=20 and imc <= 25:
    print(f'{nome} está com peso normal do peso')
elif imc >25 and imc <= 30:
    print(f'{nome} está com peso excesso do peso')
elif imc >30 and imc <= 35:
    print(f'{nome} está com obesidade')
else:
    print(f'{nome} está com obesidade mórbida')
    
    

