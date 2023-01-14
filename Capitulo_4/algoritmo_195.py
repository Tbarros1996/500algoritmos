# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 195
# Capitulo 4

"""
Criar um algoritmo que imprima a soma dos números pares entre 25 e 200.

"""

# Método 1
i = []
for contador in range(25,200+1):
    if contador % 2 == 0:
        i.append(contador)
    else:
        pass
print(f'A soma de todos os números pares Entre 25 a 200 é {sum(i)} Método 1')


# Método 2

j = 0
for contagem in range(25,200+1):
        if contagem % 2 == 0:
            j = j + contagem
        else:
            pass

print(f'A soma de todos os números pares Entre 25 a 200 é {j} Método 2')