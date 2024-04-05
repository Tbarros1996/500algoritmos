# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 244
# Capitulo 4

"""
Entrar com uma mensagem e criptogra fá-Ia da seguinte maneira:

A-X;E-Y;I-W;O-K;U-Z

"""
#Letras com sinal gráficos serão considerados outros caracteres


texto = str(input("Entre com o Texto (Sem Sinal Gráfico): "))

criptografado = list(texto)

for i in range(0,len(criptografado)):
    
    match criptografado[i]:
        
        case "A" | "a" :
            criptografado[i] = "X"
        case "E" | "e":
            criptografado[i] = "Y"   
        case "I" | "i" :
            criptografado[i] = "W"
        case "O" | "o":
            criptografado[i] = "K"
        case "U" | "u" :
            criptografado[i] = "Z"
              
print(f'Palavra Criptigrafada: {"".join(criptografado)}')


"""
O método join é o método usado para concatenar os caracteres de uma lista usando algum tipo de separador. Para utiliza-lo sempre use 
"caractere separador".join(lista)

"""