import math

conta = float(input('Digite o valor inicial: \n'))
juros = float(input('Digite a taxa de juros: \n'))
meses = int(input('Digite o tempo em meses: \n'))


juros = juros/100
mont = conta*(1+juros)

loop = 0

while(loop==0 or loop<meses):
    loop = loop+1
    print('Montante: \n', mont)
    mont = mont+(mont*juros)