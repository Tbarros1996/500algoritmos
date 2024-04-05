# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 245
# Capitulo 4

"""
Criar um algoritmo que receba a idade e o peso de 20 pessoas. Calcular e imprimir as médias dos pesos das pessoas da mesma faixa etária. As faixas etárias são: de 1 a 10 anos, de 11 a 20 anos, de 21 a 30 anos e maiores de 30 
anos.

"""

peso = []
idade = []

faixa_1_10 = []
faixa_11_20 = []
faixa_21_30 = []
faixa_30 = []

valor_registros = int(input("Entre com a quantidade de registros : "))

for i in range(0,valor_registros):
    
    valor_peso = float(input("Entre com o valor do peso : "))
    
    valor_idade = float(input("Entre com a idade : "))
    
    peso.append(valor_peso)
    
    idade.append(valor_idade)
    

for i in range(0,len(idade)):
    
    if idade[i] <= 10:
        faixa_1_10.append(peso[i])
        
    elif idade[i] > 10 and idade[i] <= 20 :
        faixa_11_20.append(peso[i])
        
    elif idade[i] > 20 and idade[i] <= 30 :
        faixa_21_30.append(peso[i])
        
    else:
        faixa_30.append(peso[i])  


total_soma = {"a":sum(faixa_1_10),"b":sum(faixa_11_20),"c":sum(faixa_21_30),"d":sum(faixa_30)}   

total_tamanho = {"A":len(faixa_1_10),"B":len(faixa_11_20),"C":len(faixa_21_30),"D":len(faixa_30)}  

if total_soma["a"] != 0:
    print(f'Peso Médio de 1 a 10 = {total_soma["a"]/total_tamanho["A"]}')
    
if total_soma["b"] != 0:
    print(f'Peso Médio de 11 a 20 = {total_soma["b"]/total_tamanho["B"]}')
    
if total_soma["c"] != 0:
    print(f'Peso Médio 21 a 30 = {total_soma["c"]/total_tamanho["C"]}')
    
if total_soma["d"] != 0:
    print(f'Peso Médio acima de 30 = {total_soma["d"]/total_tamanho["D"]}')

