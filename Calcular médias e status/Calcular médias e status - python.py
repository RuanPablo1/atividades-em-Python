import math

aluno = input("Nome do aluno: ");

matricula = input("\nMatricula do aluno: ")

nota1 = float(input("\nDigite a nota 1: \n"))
nota2 = float(input("\nDigite a nota 2: \n"))
nota3 = float(input("\nDigite a nota 3: \n"))
nota4 = float(input("\nDigite a nota 4: \n"))

media = ((nota1+nota2+nota3+nota4)/4)

print("A média é:", media,"\n")

if(media<0 or media>10):
    print("Média inválida!")

if(media>0 and media<5):
    print("O aluno",aluno,"de matrícula",matricula,"teve como média",media,"e está REPROVADO!\n")

if(media>=5 and media<6):
    print("O aluno",aluno,"de matrícula",matricula,"teve como média",media,"e está de RECUPERAÇÃO!\n")

if(media>=6 and media<=10):
    print("O aluno",aluno,"de matrícula",matricula,"teve como média",media,"e está APROVADO!\n")