# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 222
# Capitulo 4

"""
Criar um algoritmo que entre com uma 
palavra e imprima conforme o exemplo a
seguir:
input:PAZ
Output:
ZAP
"""

nome = str(input("Entre com o Nome: "))

# Método 1 (Fateamento Invertido)

"""
Revisão: Estruturas de Fateamento em Python

Estrutura: sequencia[inicio:fim:passo]

# Selecionando elementos do índice 2 ao índice 5 (exclusivo)
print(lista[2:5])  # Saída: [3, 4, 5]

# Selecionando os primeiros 3 elementos
print(lista[:3])   # Saída: [1, 2, 3]

# Selecionando os últimos 3 elementos
print(lista[-3:])  # Saída: [8, 9, 10]

# Selecionando todos os elementos com um passo de 2
print(lista[::2])  # Saída: [1, 3, 5, 7, 9]

# Invertendo a lista
print(lista[::-1])  # Saída: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Exemplo com string
texto = "Python é incrível!"

# Selecionando os caracteres do índice 7 ao índice 12 (exclusivo)
print(texto[7:12])  # Saída: é in

# Invertendo a string
print(texto[::-1])  # Saída: !levírcni é nohtyP

"""

print(nome[::-1])

# Método 2 - Usando Loop For

for x in range(len(nome)-1,-1,-1):
    print(nome[x])
 
"""
Revisão da estrutura de Range

range(inicio, fim, passo)

inverter uma palavra consiste em partir do último (maior valor negativo)
até o primeiro (menor valor negativo)

T - 0 (x in range(0,len(nome) = 6) primeira letra nome[x] = nome[0] )
H - 1 (x in range(0,len(nome) = 6) primeira letra nome[x] = nome[1] )
I - 2 (x in range(0,len(nome) = 6) primeira letra nome[x] = nome[2] )
A - 3 (x in range(0,len(nome) = 6) primeira letra nome[x] = nome[3] )
G - 4 (x in range(0,len(nome) = 6) primeira letra nome[x] = nome[4] )
O - 5 (x in range(0,len(nome) = 6) primeira letra nome[x] = nome[5] )

Geralmente eu uso o intervalo em range começando do 1 até len(x)+1 para
adequar a contagem matemática e indexação


No caso do range reverso a lógica confunde um pouco mas é simples
basicamente soma de número negativo

T - -6 
H - -5 
I - -4 
A - -3 
G - -2 
O - -1 

o início seria -6 e o final seria -1 (reveja indexação em Python)

e para o passo seria 1 porque estamos pulando número negativo

de -6 para -5 = Passo positivo 1
de -5 para -6 = Passo negativo 1


por isso se fizermos um loop for nesse formato, ele imprime a letra só
que contando com indexação negativa:

"""
for x in range(-len(nome),0):
    print(nome[x])
    


#Resumo

# Idexação positiva - Da Esquerda para Direita:

# range (primeiro positivo, último positivo, passo(opcional))

# Indexação Negativa -  Da Esquerda para Direita:

# range(menor valor negativo(primeira letra),maior valor negativo(última letra), passo(opcional porém positivo))

# Indexação de Trás pra Frente

# range(::passo negativo (obrigatório))
