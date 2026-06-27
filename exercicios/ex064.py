num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número inteiro: '))
    print('PARA PARAR O PROGRAMA, DIGITE: 999')
    if num != 999:
        soma += num
        cont += 1
print('Foram digitados {} números e a soma entre ele é {}!'.format(cont, soma))