import math


print("Para qual temperatura deseja converter?\n\n")

print("1- Celsius para Kelvin\n")
print("2- Celsius para Fahrenheit\n")
print("3- Kelvin para Celsius\n")
print("4- Kelvin para Fahrenheit\n")
print("5- Fahrenheit para Celsius\n")
print("6- Fahrenheit para Kelvin\n\n")

op = int(input("Opcao: \n"))


if(op == 1):
    tc = float(input("Digite o valor de Celsius: "))
    res = (tc-273)

if(op == 2):
    tc = float(input("Digite o valor de Celsius: "))
    res = (tc*9/5)+32

if(op == 3):
    tk = float(input("Digite o valor de Kelvin: "))
    res = (tk+273)

if(op == 4):
    tk = float(input("Digite o valor de Kelvin: "))
    res = (tk-273)*9/5+32

if(op == 5):
    tf = float(input("Digite o valor de Fahrenheit :"))
    res = (tf-32)*5/9

if(op == 6):
    tf = float(input("Digite o valor de Fahrenheit: "))
    res = (tf-32)*5/9+273

else:
    print("Opcao invalida!\n\n")


print("O resultado e: ",res,".")