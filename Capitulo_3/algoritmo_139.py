# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 139
# Capitulo 2

"""
Sabendo que somente os municípios que possuem mais de 20.000 eleitores aptos 
têm segundo turno nas eleições para prefeito caso o primeiro colocado não 
tenha mais do que 50% dos votos, fazer um algoritmo que leia o nome do 
município, a quantidade de eleitores aptos, o número de votos do candidato
mais votado e informar se ele terá ou não segundo turno em sua eleição municipal.  

"""

def resultado (nome = str, eleitores = int, votos = int , cidade = str):
    if eleitores > 20000:
        percentual = (votos/eleitores)*100
        if percentual >50:
            print(f'Canditato {nome} eleito em {cidade} com {round(percentual,2)} dos votos')
        elif percentual <50:
            print("Terá Segundo Turno")
    else:
        print("Candidato Eleito")

nome = str(input("Entre com o nome do candidato mais votado"))
cidade = str(input("Entre com o nome da Cidade"))
eleitores = int(input("Entre com o número de eleitores"))
votos = int(input("Entre com o número de votos do candidato mais votado"))

resultado(nome,eleitores,votos,cidade)

