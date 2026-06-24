num1 = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número: '))
listaNum = [num1, num2]


opcao = int(input('SUA ESCOLHA: '))
while opcao <= 5 and opcao >= 1:
    print('''
    ESCOLHA UMA DAS OPÇÕES ABAIXO:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA    
    ''')

if opcao == 1:
    print('A soma do n° {} com o n° {} é {}'.format(num1, num2, num1+num2))
elif opcao == 2:
    print('A Multiplicação do n° {} com o n° {} é {}'.format(num1, num2, num1*num2))
elif opcao == 3:
    if num1 > num2:
        print('O n° {} é maior que o m° {}'.format(num1, num2))
    elif num2 > num1:
        print('O n° {} é maior que o n° {}'.format(num2, num1))
elif opcao == 4:
    novoNum = int(input('Digite um novo número: '))
