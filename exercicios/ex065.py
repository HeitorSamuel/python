opcao =  maior = menor = soma = cont = 0

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
    print('-=' * 30)
    print('''
Você quer continuar a digitar valores?
[0] SIM
[1] NÃO
''')
    print('-=' * 30)
    opcao = int(input('Digite a sua opção: ').strip())
    print('-=' * 30)
    while opcao > 1 or opcao < 0:
        opcao = int(input('Opção inválida! Digite Novamente: ').strip())
        print('-=' * 30)    
print('A média dos números digitados foi: {:.2f}'.format(media))
print('O maior valor digitado foi {} e o menor valor digitado foi {}'.format(maior, menor))
    