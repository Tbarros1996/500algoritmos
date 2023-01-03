# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 77
# Capitulo 2


"""
Ler dois números reais e imprimir o quadrado da diferença do primeiro valor pelo 
segundo e a diferença dos quadrados. 

"""
a = float(input('Entre com o Valor: '))
b = float(input('Entre com o Valor: '))

qua_dif = (a-b)**2
dif_qua = (a**2-b**2)

print(f'Quadrado da diferença {qua_dif}')
print(f'Diferença dos Quadrados {dif_qua}')