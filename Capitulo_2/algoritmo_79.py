# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 79
# Capitulo 2


"""
Uma pessoa resolveu fazer uma aplicação 
em uma poupança programada. Para 
calcular seu rendimento, 
ela deverá fornecer o valor constante da 
aplicação mensal, a 
taxa e o número de meses. 
Sabendo-se que a fórmula usada 
para este cálculo é:

valor acumulado = P * ' . - 
i = taxa 
P = aplicação mensal 
n= número de meses

"""
i = float(input('Entre com a taxa : '))
n = float(input('Entre com o númeo de meses: '))
p = float(input('Entre com a aplicação mensal: '))

m = (p/i)*( ((1+i)**n)-1      )

print(f'Logo o montante será de R$ {round(m,2)}')