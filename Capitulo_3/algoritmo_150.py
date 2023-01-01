# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 150
# Capitulo 2

"""
Criar um algoritmo que leia um ângulo em graus e apresente: 
o seno do ângulo, se o ângulo pertencer a um quadrante par; 
o co-seno do ângulo, se o ângulo pertencer a um quadrante ímpar. 

Revisando:

          Quadrante 2  |   Quadrante 1
          ------------ |----------------
          Quadrante 3  |   Quadrante 4
                       |

"""
from math import pi as pi
from math import sin as sin
from math import cos as cos

angulo = float(input("Entre com o ângulo: "))
angulo_rad = angulo * (pi/180)

#Opcional: Código para definir o Quadrante

if angulo_rad >= 0 and angulo_rad < (pi/2):
    print("Primeiro Quadrante")
elif angulo_rad >= (pi/2) and angulo_rad < (pi):
    print("Segundo Quadrante")
elif angulo_rad >= pi and angulo_rad < ((3*(pi/2))):
    print("Terceiro Quadrante")
elif angulo_rad >= ((3*(pi/2))) and angulo_rad < (2* pi):
    print("Quarto Quadrante")
    
    

if (angulo_rad > (pi/2) and angulo_rad < pi) or (angulo_rad > (3*(pi/2)) and angulo_rad <= 2*pi):
    print(f'seno será {round(sin(angulo_rad),2)}')
else:
    print(f' logo o coseno será {round(cos(angulo_rad),2)}')
        
    

