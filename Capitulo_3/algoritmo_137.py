# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 137
# Capitulo 2

"""
Ler três valores inteiros (variáveis a, b e c) e efetuar o cálculo da equação de 
segundo grau, apresentando: as duas raízes, separa os valores informados for pos- 
sívelfazero cálculo (deita positivo ou zero); a mensagem "Não há raízes reais", se 
não for possível fazer o cálculo (deita negativo); e a mensagem "Não é equação 
do segundo grau", se o valor de a for iguala zero. 

"""
import math as mt

a = int(input("Entre com o valor Inteiro a: "))
b = int(input("Entre com o valor Inteiro b: "))
c = int(input("Entre com o valor Inteiro c: "))   

d = (b**2) - (4*a*c)

if a == 0:
    print("Não é uma Equação do Segundo Grau")
elif d>0:
    r = mt.sqrt(d)
    x1 = ((-b) + r)/(2*a)
    x2 = ((-b) - r)/(2*a)
    print(f'As raizes são {x1} e {x2}')
elif d==0:
    r = mt.sqrt(d)
    x1 = ((b))/(2*a)
    print(f'A raiz é +-{x1}')
elif d<0:
    print("Equação não possui raizes reais")
    
    