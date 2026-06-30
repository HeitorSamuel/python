#FALTA COMPLETAR
from time import sleep
num1 = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número: '))
opcao = 0

while opcao != 5:
    print('''      
ESCOLHA UMA DAS OPÇÕES ABAIXO:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA    
''')
    opcao = int(input('SUA ESCOLHA: '))
    if opcao == 1:
        sleep(1)
        print('-='*40)
        print('A soma do número {} com o número {} é {}'.format(num1, num2, num1+num2))
        print('-='*40)
    elif opcao == 2:
        sleep(1)
        print('-='*40)
        print('A Multiplicação do número {} com o número {} é {}'.format(num1, num2, num1*num2))
        print('-='*40)
    elif opcao == 3:
        if num1 > num2:
            sleep(1)
            print('-='*40)
            print('O número {} é maior que o número {}'.format(num1, num2))
            print('-='*40)
        elif num2 > num1:
            sleep(1)
            print('-='*40)
            print('O número {} é maior que o número {}'.format(num2, num1))
            print('-='*40)
        elif num1 == num2:
            sleep(1)
            print('-='*40)
            print('Não há nunhum número MAIOR! Ambos são iguais a {}!'.format(num1))
            print('-='*40)
    elif opcao == 4:
        print('-='*40)
        num1 = float(input('Digite o 1° número: '))
        num2 = float(input('Digite o 2° número: '))
        print('-='*40)
    elif opcao < 1 or opcao > 5:
        sleep(1)
        print('-='*40)
        print('Opção Inválida! Tente Novamente!')
        print('-='*40)
print('-='*20)
print('PROCESANDO...')
print('-='*20)
sleep(1.5)
print('FIM DO PROGRAMA!')
