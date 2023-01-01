# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 103
# Capitulo 2


"""
Entrar com o ano de nascimento de uma pessoa e o ano atual. Imprimira idade da
pessoa. Não se esqueça de verificar se o ano de nascimento é um ano válido.


"""

import time as tm
atual = int(tm.strftime("%Y"))
nascimento = int(input(print("Entre com o ano")))

if nascimento < atual:
    idade = atual - nascimento
    print(f"A idade é {idade}, anos")
elif nascimento > atual:
    print("Você não nasceu ainda")
