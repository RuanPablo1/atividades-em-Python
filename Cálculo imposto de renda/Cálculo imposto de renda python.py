import math

calculo = float(input("Digite o valor do seu salário com o desconto do INSS: "))

pensao = float(input("\nQuanto você paga de pensão alimentícia? \n"))

dependentes = int(input("\nQuantos dependentes você possui?\n"))

dd = dependentes*189.59 #"dd" (Desconto dependente) É o valor fixo que é descontado sobre cada dependente.
salario = calculo - pensao - dd #Salário já retirando o desconto do INSS, pensão alimentícia e taxa fixa sobre cada dependente.


if (salario >= 1903.99 and salario <= 2826.65):
    print("Você está na faixa de cálculo 1!;\n")
    print("A aliquota e de 7.5% !\n")
    porc = (salario * 0.075)
    resultado = porc - 142.8
    print("O desconto total do seu imposto de renda é de", resultado)


elif (salario >= 2826.66 and salario <= 3751.05):
    print("Você está na faixa de cálculo 2!;\n")
    print("A aliquota e de 15% !\n")
    porc = (salario * 0.15)
    resultado = porc - 354.8
    print("O desconto total do seu imposto de renda é de", resultado)


elif (salario >= 3751.06 and salario <= 4664.68):
    print("Você está na faixa de cálculo 3!;\n")
    print("A aliquota e de 22.5% !\n")
    porc = (salario * 0.225)
    resultado = porc - 636.13
    print("O desconto total do seu imposto de renda é de", resultado)


elif (salario > 4664.69):
    print("Você está na faixa de cálculo 4!;")
    print("A aliquota é de 27.5% !")
    porc = (salario * 0.275)
    resultado = porc - 869.36
    print("O desconto total do seu imposto de renda é de", resultado)

else:
    print("\nNão é necessário declarar imposto de renda!")

#Fonte utilizada para a lógica do cálculo: https://blog.convenia.com.br/como-calcular-irrf-na-folha-de-pagamento/