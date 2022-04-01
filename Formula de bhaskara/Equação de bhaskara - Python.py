import math


A = float(input('Digite o valor de A: '))
B = float(input('Digite o valor de B: '))
C = float(input('Digite o valor de C: '))

delta = (B*B)-(4*A*C)
print (delta)

if delta>=0:
    print ("O delta e igual a: ", delta)

else:
    print ("Delta invalido!")
    

print("Calculando as raizes de delta.")

x1 = (-B+math.sqrt(delta))/(2*A)
x2 = (-B-math.sqrt(delta))/(2*A)

print("O x1 é igual a: \n" , x1)

print("O x2 é igual a: \n" , x2)


