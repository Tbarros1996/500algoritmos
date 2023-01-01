# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 100
# Capitulo 2


# Nota: A questão apresentava uma resolução diferente do que pedia logo se fez diferente


"""
Ler um número inteiro de 4 casas e imprimir se é ou não múltiplo de quatro o nú-
mero formado pelos algarismos que estão nas casas das unidades de milhar e das
centenas.

"""

valor = str(input(print("Entre com o valor de Digitos")))
valor_inteiro = int(valor)
valor_lista = list(valor)
centena = int(valor_lista[1])
unidade = int(valor_lista[3])
#Verificação

print(f"Centena é {centena}, Unidade é {unidade}, valor é {valor_inteiro}")
if (valor_inteiro % centena == 0):
    if (valor_inteiro % unidade == 0):
        print("O valor é multiplo da centena e da Unidade")
    elif (valor_inteiro % unidade !=0):
        print("O número é multiplo pela centena mas não pela Unidade ")
else:
    print("O número não é multiplo nem pela centena e nem pela unidade")
        



