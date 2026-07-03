somaIdade = maiorIdade = quantMulher = 0
nomeMaiorIdade = ''

for c in range(1, 5):
    print('{:=^40}'.format(' {}ª pessoa '.format(c)))
    nome = str(input('Digite o seu nome: ')).strip().capitalize()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo: ')).strip().upper()
    somaIdade += idade
    if sexo == 'MASCULINO':
        if idade > maiorIdade:
            maiorIdade = idade
            nomeMaiorIdade = nome
    elif sexo == 'FEMININO':
        if idade < 20:
            quantMulher += 1

print('='*40)
print('A MÉDIA DE IDADE do grupo é: {:.1f}'.format(somaIdade/4))
print('O nome do HOMEM MAIS VELHO é: {}. Ele tem {} anos!'.format(nomeMaiorIdade, maiorIdade))
print('A quantidade de mulheres que têm MENOS DE 20 ANOS é: {}'.format(quantMulher))

print('='*40)