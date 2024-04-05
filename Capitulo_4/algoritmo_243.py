# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 243
# Capitulo 4

"""
Entrar com uma mensagem e imprimir quantas letras A E / O e U tem esta men-
sagem (considerar minúscula e maiúscula).

"""
# Usando um laço e Match Case

#Letras com sinal gráficos serão considerados outros caracteres
# portanto, caso maior quantidade de variação de vogais, convém uma lista

texto = str(input("Entre com o Texto (Sem Sinal Gráfico): "))

for i in range(len(texto)):
    
    match texto[i]:
        
        case "A" | "a" :
            ca += 1
        case "E" | "e":
            ce += 1   
        case "I" | "i" :
            ci += 1
        case "O" | "o":
            co += 1
        case "U" | "u" :
            cu += 1
              
print(f'Total de A: {ca}')
