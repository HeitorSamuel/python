num = int(input('Digite um número inteiro: '))
contDivisores = 0

if num <= 1:
    print('O número {} não é um número primo!'.format(num))
else:
    for c in range(1, (num+1)):
        if num % c == 0:
            contDivisores += 1
    if contDivisores == 2:
        print('O número {} é um número PRIMO! Ele possui {} divisores!'.format(num, contDivisores))
    elif contDivisores > 2:
        print('O número {} é um número COMPOSTO! Ele tem {} divisores!'.format(num, contDivisores))

