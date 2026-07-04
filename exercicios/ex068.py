from random import randint

print('-='*25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*25)

jogador = int(input('Digite um número: '))

escolhaJog = str(input('Par ou Ímpar? [P/I] ')).strip()[0]

computador = randint(0, 10)

somaNum = computador + jogador

print(somaNum)
