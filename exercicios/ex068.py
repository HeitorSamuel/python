from random import randint

print('-='*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*30)

vitoria = 0

while True:
    
    jogador = int(input('Digite um número: '))

    comput = randint(0, 10)

    somaNum = comput + jogador

    escolhaJog = ' '
    
    while escolhaJog != 'P' and escolhaJog != 'I':
        escolhaJog = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    if somaNum % 2 == 0:
        resultado = 'P'
        resp = 'PAR'
    else:
        resultado = 'I'
        resp = 'ÍMPAR'
    print('-'*60)
    print(f'Você jogou {jogador} e o computador {comput}. Total de {somaNum} DEU {resp}')
    print('-'*60)
    if escolhaJog == resultado:
        print('Você VENCEU!')
        print('Vamos Jogar novamente...')
        print('-='*30)
        vitoria += 1
    else:
        print('Você PERDEU!')
        print('-='*30)
        break

print(f'GAME OVER! Você venceu {vitoria} vez(es)')