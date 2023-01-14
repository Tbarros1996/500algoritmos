# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 191
# Capitulo 4

"""
Criar um algoritmo que leia um nÚmero que será o limite suprior de um intervalo e 
o incremento (incr) Imprimir todos os numeros naturais no intervalo de O ate esse 
numero Suponha que os dois numeros lidos são maiores do que zero Exemplo 

"""
ls =int(input("Entre com a Limite Superior: "))
incre =int(input("Entre com o Incremento: "))

for contador in range(0,ls+incre,incre):
    print(contador)
    
    
    
