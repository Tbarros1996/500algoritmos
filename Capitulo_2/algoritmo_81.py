# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 81
# Capitulo 2

"""
Criar um algoritmo que, dado um número de conta corrente com três dígitos, 
retorne o seu dígito verificador, 
o qual é calculado da seguinte maneira:
Exemplo: número da conta: 235 
Somar o número da conta com o seu inverso: 235+ 532 = 767 
multiplicar cada dígito pela sua ordem posicional e somar estes resultados: 767 

"""

conta = str(input("Digite a Conta de 3 digitos: "))
rev = conta[::-1]
soma = int(conta) + int(rev) 
produto = int(str(soma)[0])*1 + int(str(soma)[1])*2 + int(str(soma)[2])*3
final = str(produto)
digito = int(final[len(final)-1])
print(f'O digito verificador é {digito}')


