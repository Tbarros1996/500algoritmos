# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 155
# Capitulo 2

"""
Ler uma palavra e, se ela começar pela letra L ou D (também deve ser considerado 
1 ou d), formar uma nova palavra que terá os dois primeiros caracteres e o último, 
caso contrário a nova palavra será formada por todos os caracteres menos o primeiro. 

"""

palavra = str(input("Entre com a palavra: "))

lista = list(palavra.strip())



if (lista[0] == "l" or lista[0] == "L") or (lista[0] == "d" or lista[0] == "D"):
    print("A nova palavra é: ")
    print(str(lista[0]+lista[1]+lista[-1]))
else:
    saida = lista[1:]
    virgula = ""
    saida = virgula.join(saida) #Lembrando que o método join precisa do separador, nesse caso ""
    print(saida)


