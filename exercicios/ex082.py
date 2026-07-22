numTot = []
numPar = []
numImpar = []

while True:
    num = int(input('Digite um número: ').strip())
    numTot.append(num)
    if num % 2 == 0:
        numPar.append(num)
    elif num % 2 == 1:
        numImpar.append(num)
    perg = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    while perg not in 'S' and perg not in 'N':
        perg = str(input('Caracter inválido! Quer continuar? [S/N] ').strip().upper()[0])
    if perg == 'N':
        break
print('-='*30)
print(f'A lista completa é {numTot}')
print(f'A lista de pares é {numPar}')
print(f'A lista de ímpares é {numImpar}')