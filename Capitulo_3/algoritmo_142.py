# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 142
# Capitulo 2

"""
Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores 
para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o 
mesmo número de pontos, criar um algoritmo que informe se uma equipe foi 
classificada, de acordo com a seguinte especificação: 

* ler os pontos obtidos por cada jogador da equipe; 
* mostrar esses valores em ordem decrescente; 
* se a soma dos pontos for maior do que 100, imprimir a média aritmética 
entre eles; senão, imprimir a mensagem "Equipe desclassificada '

"""
p1,p2,p3 = int(input("Entre com a Pontuação 1 [>]")),int(input("Entre com a Pontuação 2 [>]"))\
    ,int(input("Entre com a Pontuação 3 [>]"))
pontos = [p1,p2,p3]
ordem = sorted(pontos)
print("A Ordem de classificação foi: ", ordem[-1] , ordem[-2] , ordem[-3] )
if p1+p2+p3 > 100:
    print(f'Pontuação Média de {(p1+p2+p3)/3}')
else:
    print("Equipe Desclasclassificada")
    

