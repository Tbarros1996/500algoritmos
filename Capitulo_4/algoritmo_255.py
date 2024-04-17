# 500 Exercícios Resolvidos com Python
# Thiago Barros
# Exercícios resolvidos com base no Livro - 500 Algoritimos Resolvidos (ANITA LOPES E GUTO GARCIA)
# Algoritimo Numero 255
# Capitulo 4

"""
Criar um algoritmo que entre com dez notas de cada aluno de uma turma de 20
alunos e imprima:
- a média de cada aluno
- a média da turma
- o percentual de alunos que tiveram medias maiores ou iguais a 5.0.
"""


import time as tm   
        
alunos = []
banco = {aluno:[] for aluno in alunos}

def acessar_nota(): 
    
    if not banco:
        print('O Banco de Dados Está Vazio')
        main()
    else:
        print(banco)
        main()
    
def acessar_media(aluno): 
    
    if not banco:
        print('O Banco de Dados Está Vazio')
        main()
            
    elif aluno in banco:
        media = sum(banco[aluno])/len(banco[aluno])
        return media 
    
def media_turma():  
    
    notas = []
    for aluno in banco():
        notas.append(banco[aluno])
    media = sum(notas)/len(notas)
    return media 

def aprovados():  
    
    i = 0
    notas = []
    for aluno in banco():
        notas.append(banco[aluno])
    for k in notas():
        if k >= 5:
            i =+ 1
    return i

def add_aluno():  
    
    global alunos
    global banco
    
    print('Entre com o Nome do Aluno: ')
    nome = str(input('>>>: '))
    
    if nome in banco:
        print('O aluno já foi cadastrado: ')
        print('Adicione a Nota do Aluno ')
        nota = float(input('>>>: '))
        banco[nome].append(nota)
    else:
        alunos.append(nome)
        banco = {aluno:[] for aluno in alunos}
        print('O aluno já foi cadastrado: ')
        print('Adicione a Nota do Aluno ')
        nota = float(input('>>>: '))
        banco[nome].append(nota)
             
def main(): 
    
    print("Entre com o Comando no Terminal: ")
    
    print("1 - Acessar o Banco de Dados ")
    print("2 - Acessar a Média de Um Aluno Específico ")
    print("3 - Verificar a Média da Turma ")
    print("4 - Verificar o Percentual de Aprovados ")
    print("5 - Adicionar Aluno") 
    
    entrada_1 = int(input('>>>: ')) 
       
    match entrada_1:   
         
        case 1:
            
            acessar_nota()    
                            
        case 2:
                       
            print("Entre com o nome do aluno:  ")
            
            entrada_2 = str(input('>>>: '))   
                   
            if entrada_2 in banco:
                
                print(f'As notas do aluno {entrada_2} são {banco[entrada_2]}')     
                main()     
                 
            else:
                
                print(f'As notas do aluno {entrada_2} não foram registradas no banco de dados')      
                       
                print("Deseja registrar notas?[y,n] ")
                
                entrada_3 = str(input('>>>: '))
                
                match entrada_3:
                               
                    case "y":
                        add_aluno()
                        main()
                        
                    case "n":
                        main()
        case 3:
            print(f'A média da turma é de {media_turma()}')
            main()
        
        case 4:
            print(f'O Percentual de Aprovados é de {aprovados()}')
        
        case 5:
            add_aluno()
            main()
                                    
                        

print("Banco de Dados de Nota de Alunos ")
print("Escrito por Thiago Barros ")  
tm.sleep(3)          
         
main()                       
                        
                    
                    
                