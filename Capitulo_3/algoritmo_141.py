# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 141
# Capitulo 2

"""
Criar um algoritmo que leia o nome e o total de pontos de três finalistas de um 
campeonato de pingue-pongue e exibir a colocação da seguinte forma: 
Vencedor:_______ XXXX ptos 
Segundo colocado: XXXX ptos 
Terceiro colocado: XXXX ptos 

"""
# Utilizando variáveis em sequencia

vencedor,pontuacao_1 = str(input("Entre com o nome do vencedor: ")), int(input("Entre com a pontuacao do primeiro: "))
segundo,pontuacao_2 = str(input("Entre com o nome do segundo: ")), int(input("Entre com a pontuacao do segundo: "))
terceiro,pontuacao_3 = str(input("Entre com o nome do terceiro: ")), int(input("Entre com a pontuacao do terceiro: "))
print(f'Vencedor:{vencedor} - {pontuacao_1} Pontos \n Segundo Colocado:{segundo} - {pontuacao_2} Pontos \n \
    Terceiro Colocado:{terceiro} - {pontuacao_3} Pontos')
