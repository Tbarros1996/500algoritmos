# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 105

# Capitulo 2

# Algoritmo usando o Python 3.10 utilizando o caso do mach case


"""
Entrar com a sigla do estado de uma pessoa e imprimir uma das mensagens:
carioca
m paulista
mineiro
m outros estados

"""

sp = ("SP","sp")

mg = ('MG','mg')

rj = ("RJ","rj")

sigla = str(input(print("Entre com a sigla [MG;SP;RJ]")))

if sigla == mg[0] or sigla == mg[1]:
    print("MINAS GERAIS")
elif sigla == rj[0] or sigla == rj[1]:
    print("RIO DE JANEIRO")   
elif sigla == sp[0] or sigla == sp[1] :
    print("SÃO PAULO")  
else:
    print("Demais Estados")
