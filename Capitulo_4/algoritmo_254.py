# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 254
# Capitulo 4

"""
Criar um algoritmo que entre com dez notas de cada aluno de uma turma de 20
alunos e imprima:
- a média de cada aluno
- a média da turma
- o percentual de alunos que tiveram medias maiores ou iguais a 5.0.
"""

banco = int(input("Entre Com a Quantidade de Registros: "))

registro_aluno = [f'Aluno_{k}' for k in range(banco)]
registro_geral = {chave:[] for chave in registro_aluno}
banco_geral = []
i = 0

for aluno in registro_aluno:
    
    print(f'Entre com a Nota do Aluno {aluno }')
    nota = float(input( ) )
    registro_geral[aluno].append(nota)
    banco_geral.append(nota)
    
for notas in banco_geral:
    if notas >= 5:
        i += 1

print(f'A média da Turma é de {sum(banco_geral)/len(banco_geral)}')    
print(f'O Percentual de Aprovação foi de {i/len(banco_geral)*100}%')
    
    
    
    

    

    
    


