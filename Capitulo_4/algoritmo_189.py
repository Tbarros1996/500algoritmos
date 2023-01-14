# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 189
# Capitulo 4

"""
Criar um algoritmo que imprima a tabela de conversão de graus Celsius-Fahrenheit 
para o intervalo desejado pelo usuário. O algoritmo deve solicitar ao usuário o li - mite superior, o limite inferior do intervalo e o decremento. 
Fórmula de conversão: C =5 (F - 32) / 9 
"""

import numpy as np
c = []
f1 = int(input('Entre com o limite inferior °F: '))
f2 = int(input('Entre com o limite superior °F: '))
lista = np.arange(f1,f2,1)
f = np.ndarray.tolist(lista)
i = len(f)
for x in range(0,i):
    convesao = (5*(f[x]-32))/9
    c.append(convesao)
    print(f'{round(f[x],2)} °F ----- {round(c[x],2)} °C')

# Extra: Plotando a Curva de Graus C° por Graus °F
zero = np.zeros(len(f))
import matplotlib.pyplot as plt

plt.plot(c,f,"--go")
plt.plot(c,zero,"-r")
plt.xlabel('°C')
plt.ylabel('°F')
plt.show()
