import math

dividendo = int(input("Digite um número para saber se ele é divisível por 3 e 5: "))

resto3 = dividendo%3
resto5 = dividendo%5

if(resto3==0 and resto5==0):
	print("\nO número é divisivel por 3 e 5.\n")


else:
	print("\nO número NÃO é divisivel por 3 e 5.\n")