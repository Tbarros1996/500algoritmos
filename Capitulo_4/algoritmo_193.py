# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 193
# Capitulo 4

"""
Criar um algoritmo que leia um número que servirá para 
controlar os números pares que serão impressos a partir de 2. 

"""
ls =int(input("Entre com a Limite Superior: "))
i = 0
print("Indice ---- Par")
for contador in range(0,ls+ls):
    if contador % 2 == 0 :
        i += 1
        print(f"{i}  :  {contador}")
    else:
        pass