# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 104
# Capitulo 2


"""
Entrar com nome, sexo e idade de uma pessoa. Se a pessoa for do sexo feminino e
tiver menos que 25 anos, imprimir nome e a mensagem: ACEITA. Caso contrário,
imprimir nome e a mensagem: NÃO ACEITA. (Considerar f ou F.)

"""
import time
nome = str(input(print("Entre com o Nome \a ")))
idade = int(input(print("Entre com a idade\a ")))
sexo = str(input(print("Entre com o Sexo [M;F]\a ")))

if sexo == ["F","f","Feminino","FEMININO","feminino"] and idade < 25:
    print("Processando...")
    time.sleep(2)
    print(f"Parabéns {nome}, você foi aceita")
else:
     print("Processando...")
     time.sleep(2)
     print("Desculpe, você foi recusado(a)")