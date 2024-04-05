# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 253
# Capitulo 4

"""
Criar um algoritmo que entre com dez mensagens, e, para cada mensagem, im-
primir quantas letras A tem (considerar maiúsculas e minúsculas).

"""

def conta(palavra):
    
    contagem = 0
    
    for j in palavra:
        if j == "A" or j == "a":
            contagem += 1
            
    print(f'A palavra tem {contagem} letras A')        
                        
for i in range(10):
    mensagem = str(input("Entre com a Mensagem: "))
    conta(mensagem)
