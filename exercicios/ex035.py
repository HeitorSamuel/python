retaA = float(input('Digite o valor da 1ª reta: '))
retaB = float(input('Digite o valor da 2ª reta: '))
retaC = float(input('Digite o valor da 3° reta: '))

if abs(retaB-retaC) < retaA < retaB+retaC and abs(retaA-retaC) < retaB < retaA+retaC and abs(retaA-retaB) < retaC < retaA+retaB:
    print('As retas {}, {} e {} podem formar um triangulo!'.format(retaA, retaB, retaC))
else:
    print('As retas {}, {} e {} não podem formar um triângulo!'.format(retaA, retaB, retaC))