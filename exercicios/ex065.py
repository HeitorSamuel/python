opcao = -1
while opcao != 1:
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    media = soma/cont

    print('''
Você quer continuar a digitar valores?
[0] SIM
[1] NÃO
''')
    