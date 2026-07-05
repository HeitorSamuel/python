from random import randint

print('-='*25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*25)

resultado = ''
escolhaJog = ''
vitoria = 0

while escolhaJog == resultado:
    
    jogador = int(input('Digite um número: '))

    escolhaJog = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    comput = randint(0, 10)

    somaNum = comput + jogador

    if somaNum % 2 == 0:
        resultado = 'P'
        print(f'Você jogou {jogador} e o computador {comput}. Total de {somaNum} DEU PAR')
    elif somaNum % 2 == 1:
        resultado = 'I'
        print(f'Você jogou {jogador} e o computador {comput}. Total de {somaNum} DEU ÍMPAR')
    
    vitoria += 1
    print('Você VENCEU!')
    print('Vamos Jogar novamente...')

print('Você PERDEU!')
print(f'GAME OVER! Você venceu {vitoria} vez(es)')