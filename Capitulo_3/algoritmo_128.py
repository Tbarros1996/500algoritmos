# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 128
# Capitulo 3


"""
Entrar com um verbo no infinitivo e imprimir uma das mensagens: 
m verbo não está no infinitivo 
m verbo da 1°conjugação 
m verbo da 2°conjugação 
m verbo da 3°conjugação 
"""

verbo = str.lower(input("Entre com o verbo: "))


if verbo[len(verbo)-2] == "a":
    print("Primeira Conjugação")
elif verbo[len(verbo)-2] == "e":
    print("Segunda Conjugação")
elif verbo[len(verbo)-2] == "i":
    print("Terceira Conjugação")
else:
    print("Verbo em outro tempo verbal")

