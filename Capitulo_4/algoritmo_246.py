# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 246
# Capitulo 4

"""

No dia da estréia do filme "Senhor dos Anéis ', uma grande emissora de TV reali -
zou uma pesquisa logo após o encerramento do filme. Cada espectador respon-
deu a um questionário no qual constava sua idade e a sua opinião em relação ao
filme: excelente -3; bom -2; regular- 1. Criar um algoritmo que receba a idade
e a opinião de 20 espectadores, calcule e imprima:
a média das idades das pessoas que responderam excelente;
m a quantidade de pessoas que responderam regular;
a percentagem de pessoas que responderam bom entre todos os
expectadores analisados.

"""


amostras = int(input('Entre com o número de Amostras: '))

excelente = 0
bom = 0
regular = 0

lista_idade = []
lista_avaliacao = []

for i in range(0,amostras):
    
    idade = int(input('Entre com a Idade: '))
    avaliacao = int(input('Entre com a Avaliação: '))
    lista_idade.append(idade)  
    lista_avaliacao.append(avaliacao)


for k in range(0,amostras):
    
    if lista_avaliacao[k] != 0:
        if lista_avaliacao[k] == 3:
            excelente += 1
        elif lista_avaliacao[k] == 2:
            bom += 1
        elif lista_avaliacao[k] == 1:
            regular += 1

print(f'Idade Média dos Intrevistados = {sum(lista_idade)/amostras}')
print(f'Quantidade de "Regular = {regular}')
print(f'% de Respostas "Bom" = {(bom/len(lista_avaliacao)*100)}') 


