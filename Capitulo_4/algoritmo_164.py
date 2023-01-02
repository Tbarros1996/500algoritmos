# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 164
# Capitulo 4

"""
Algoritmo que simula pausa

"""
i = 0
for i in range(0,50001):
    if i == 0:
        print("Começou")
    elif i==50000:
        print("Terminou")
    else:
        print("Contando",i)
    