from random import randint

print('-='*25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*25)

resultado = ''
escolhaJog = ''
vitoria = 0

while True:
    
    jogador = int(input('Digite um número: '))

    escolhaJog = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    comput = randint(0, 10)

    somaNum = comput + jogador

    if somaNum % 2 == 0:
        resultado = 'PAR'
        print(f'Você jogou {jogador} e o computador {comput}. Total de {somaNum} DEU {resultado}')
        if escolhaJog == resultado[0]:
            print('Você VENCEU!')
            print('Vamos Jogar novamente...')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break

    elif somaNum % 2 == 1:
        resultado = 'ÍMPAR'
        print(f'Você jogou {jogador} e o computador {comput}. Total de {somaNum} DEU {resultado}')
        if escolhaJog == resultado[0]:
            print('Você VENCEU!')
            print('Vamos Jogar novamente...')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
print(f'GAME OVER! Você venceu {vitoria} vez(es)')