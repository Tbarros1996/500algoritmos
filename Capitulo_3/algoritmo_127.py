# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 127
# Capitulo 2


"""
Entrar com nome, nota da PR
 e nota da PR2 de um aluno. Imprimir nome, nota
da PR1, nota da PR2, média e uma das mensagens: Aprovado, Reprovado ou em
Prova Final 
(a média é 7 para aprovação, menor que 3 para reprovação e as demais em prova final).
"""
nome = str(input('Entre com o Nome do Aluno'))
nota = float(input('Entre com a nota'))

if nota >= 7:
    print(f'{nome} está APROVADO')
else:
    if nota < 3:
        print(f'{nome} está REPROVADO')
    else:
        print(f'{nome} está em RECUPERAÇÃO')