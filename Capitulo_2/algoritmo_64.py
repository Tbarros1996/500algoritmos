# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 64
# Capitulo 2
"""

Ler uma temperatura em graus centígrados e apresentá-la convertida em graus
Fahrenheit. A formula de conversão e:F = onde F e a temperatura em
Fahrenheit e C é a temperatura em centígrados.

"""

def c_to_f(c = float):
    """[Conversão de Temperatura]
    Args:
        c ([Float], optional): [Temperatura em °C]. Defaults to float.

    """
    f = ((c*9)/5)+32
    print(f"A temperatura é:  {f}")
    return f
    

x = (c_to_f(0))


