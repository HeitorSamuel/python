opcao = 0
maior = 0
menor = 0
soma = 0
cont = 0
while opcao == 0:
    num = int(input('Digite um número: ').strip())
    soma += num
    cont += 1
    media = soma/cont
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    print('-=' * 40)
    print('''
Você quer continuar a digitar valores?
[0] SIM
[1] NÃO
''')
    print('-=' * 40)
    opcao = int(input('Digite a sua opção: ').strip())
    print('-=' * 40)
    while opcao > 1 or opcao < 0:
        opcao = int(input('Opção inválida! Digite Novamente: ').strip())
        print('-=' * 40)    
print('A média dos números digitados foi: {:.1f}'.format(media))
print('O maior valor digitado foi {} e o menor valor digitado foi {}'.format(maior, menor))
    