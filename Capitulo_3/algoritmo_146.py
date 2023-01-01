# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 146
# Capitulo 2

"""
Fazer um algoritmo que leia o percurso em quilômetros, o tipo do carro e informe 
o consumo estimado de combustível, sabendo-se que um carro tipo C faz 12 km 
com um litro de gasolina, um tipo B faz 9 km e o tipo C, 8 km por litro. 

"""
def consumo (tipo = str,km = float ):
    if (tipo == "A") or (tipo == "a"):
        return 12 * km
    elif (tipo == "B") or (tipo == "b"):
        return 9 * km
    elif (tipo == "C") or (tipo == "c"):
        return 8 * km
        

print("Entre com o percurso realizado: ")

km = float(input("[Distância em KM]: "))

print("Entre com o tipo de carro [A - 12 KM/L , B - 9 KM/L ,C - 8 KM/L]: ")

tipo = str(input("[Tipo Carro]: "))

valor = consumo(tipo,km)

print(f'Seu carro é do tipo {tipo}, e nesse percurso foi consumido {valor} Litros')
