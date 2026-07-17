numExten = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numInt = int(input('Digite um número entre 0 e 20: ').strip())
    print('-'*40)
    while numInt < 0 or numInt > 20:
        numInt = int(input('Tente Novamente! Digite um número entre 0 e 20: ').strip())
        print('-'*40)
    print(f'Você digitou o número {numExten[numInt]}!')
    print('-'*40)
    perg = str(input('Quer continuar? [S/N] ').strip().upper())
    print('-'*40)
    while perg != 'S' and perg != 'N':
        perg = str(input('Opção Inválida! Quer continuar? [S/N] ').strip().upper())
    if perg == 'N':
        break
print('FIM DO PROGRAMA!')