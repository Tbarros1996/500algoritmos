# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 47
# Capitulo 2
"""
Entrar com um número no formato CDU e imprimir invertido: UDC. (Exemplo:
123, sairá 321.) O número deverá ser armazenado em outra variável antes de ser
impresso.

"""


valor_centena = (input((print("Entre com um valor  : "))))
valor_invertido = [d for d in valor_centena] # Separa o valor em uma lista
valor_invertido = valor_invertido[::-1] # Gera uma nova lista com Elementos contados apartir do ultimo
retorno = "".join(valor_invertido)
print(float(retorno))



