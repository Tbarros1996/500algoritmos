# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 71
# Capitulo 2
"""
Criar um algoritmo que leia um valor de hora e informe quantos minutos se pas -
saram desde o iníciõ do dia.

"""

# Usando o Módulo Time para Definir a Hora Atual do Sistema

import time

agora = time.ctime()
agora_lista = agora.split()
hora_atual = agora_lista[3]
minutu_atual = agora_lista[4]
hora_final = hora_atual.split(":")
minuto_final = hora_final[1]
minutos_totais = (int(hora_final[0]))*60 + int(minuto_final)
print("\a")
print(f"Se Passaram {minutos_totais} minutos desde o Inicio do Dia")

