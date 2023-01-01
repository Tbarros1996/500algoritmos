# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 153
# Capitulo 2

"""
O prefeito do Rio de Janeiro contratou uma firma especializada para manter os níveis 
de poluição considerados ideiais para um país do 1° mundo. As indústrias, maiores 
responsáveis pela poluição, foram classificadas em três grupos. Sabendo-se que a 
escala utilizada varia de 0,05 e que o índice de poluição aceitável até 0, 25, fazer um 
algoritmo que possa imprimir intimações de acordo com o índice e a tabela a seguir: 
índice indústrias que receberão intimação 

índice indústrias que receberão intimação 
0,3 1° grupo 
0,4 1° e 2°grupos 
0.5 1°, 2° e 3° grupos

"""

def poluicao_nivel(nivel = float):
    if nivel >= 0.5:
        print("Suspender as atividade sas industrias dos grupos 1° 2° e 3°")
    elif nivel >= 0.4 and nivel < 0.5:
        print("Suspender as atividade sas industrias dos grupos 1° 2° ")
    elif nivel >= 0.3 and nivel < 0.4:
        print("Suspender as atividade sas industrias dos grupo 1°")
    else:
        print("Níveis de poluição aceitáveis")
        
        
print("Entre com o nível: ")
nivel = round(float(input()),2)
poluicao_nivel(nivel)





