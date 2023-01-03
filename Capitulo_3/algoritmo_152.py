# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 152
# Capitulo 3

"""
Criar um algoritmo que a partir da idade e peso do paciente calcule a dosagem de 
determinado medicamento e imprima a receita informando quantas gotas do 
medicamento o paciente deve tomar por dose.

Considere que o medicamento em  questão possui 500 mg por ml e que cada ml corresponde a 20 gotas 

-Adultos ou adolescentes desde 12 anos, inclusive, se tiverem peso igual ou 
acima de 60 quilos devem tomar 1000 mg; com peso abaixo de 60 quilos devem 
tomar 875 mg. 

-Para crianças e adolescentes abaixo de 12 anos é dosagem é calculada pelo 
peso corpóreo conforme a tabela a seguir: 

5 kg a 9 kg = 125 mg

24.1 kg a 30kg = 500mg

9.1 kg a 16 kg = 250 mg

161 kg a 24kg = 375 mg 

Acima de 30 kg = 750 mg 

"""

idade = int (input("Entre com a Idade: "))
peso = float (input("Entre com o Peso em KG: ") )
gotas = 500/20


if idade >=12:
    if peso >= 60:
        print(f'A Dosagem é de {round(1000/gotas)} gotas')
    else:
        print(f'A Dosagem é de {875/gotas} gotas')

        
if idade < 12:
    if peso < 5:
        print("Não pode tomar remédio porque o peso é muito baixo, favor consultar o médico")
    elif peso >= 5 and peso <= 9:
        print(f'Deve-se tomar {round(125/gotas,)} gotas')
    elif peso >= 9.1 and peso <= 16:
        print(f'Deve-se tomar {round(250/gotas)} gotas')
    elif peso >= 16.1 and peso <= 24:
        print(f'Deve-se tomar {round(375/gotas)} gotas')
    elif peso >= 24.1 and peso <= 30:
        print(f'Deve-se tomar {round(500/gotas)} gotas')
    elif peso >30:
        print(f'Deve-se tomar {round(750/gotas)} gotas')
        
        
"""
Comentário do Editor:

Esse exercício é importante pois mostra um pouco da responsabilidade 
do desenvolverdor de software. Uma resposta errada por causa de uma 
condicinal não construida de maneira correta pode ocasionar um erro de dosagem, o que tem impacto
direto no paciente e afeta não só a eficácia da aplicação do remédio mas pode ocasionar agravamento
do problema.

Outro ponto a destacar é o erro numérico. Pelo resultado da aplicação ser uma quantidade de gotas resultante
de um quociente entre valores, um resultado de gotas pode também ser um float, mas não é possivel
mensurar uma gota parcial (Não existe meia gota ??). A decisão de arrendondar para mais ou menos gera um erro numérico, o que 
talvez na aplicação aqui não deva ocasionar danos, mais em aplicações mais complexas, ex: projeção de
trajetórias, precisão de usinagem, é correto dizer que o erro numérico vai gerar ruido.



"""          





