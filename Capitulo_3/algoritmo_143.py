# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 143
# Capitulo 3

"""
Criar um algoritmo que verifique 
a(s) letra(s) central(is) de uma palavra 
Se o numero de caracteres for ímpar, 
ele verifica se a letra central é uma vogal; 
caso contrario verifica se e um dos digrafos 
rr ou ss (só precisa, testar letras minusculas) 
"""

vogal = ["a","e","i","o","u"]
palavra = list((input("Entre com a Palavra: ").lower()))
l = len(palavra)
digrafo = ["ss","rr"]

if l <= 2:
    print("A palavra não possui caracteres suficientes para determinar o meio")
else:
    if (l % 2 ) != 0:
        i = int((l-1) - ((l-1)/2))
        print(f'A letra central é : {palavra[i]}') 
        if palavra[i] in vogal:
            print("A letra é uma vogal")
        else:
            print("A letra é uma consoante")
    else:
        j = int((l/2) - 1)
        a1 = palavra[j]
        a2 = palavra[j+1]
        
        if (a1+a2) in digrafo:
            print("A palavra é par mas e contem os digrafos rr e ss NO CENTRO ")
            print("No centro é ", a1+a2)
        else:
            print("A palavra é par mas não contem os digrafos rr e ss NO CENTRO")
            print("No centro é ", a1+a2)
    



