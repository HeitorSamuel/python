somaIdade = 0
maiorIdade = 0
QuantMulher = 0
NomeMaiorIdade = ''

for c in range(1, 5):
    print('-='*20)
    nome = str(input('Digite o seu nome: ')).strip().lower()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo: ')).strip().lower()
    somaIdade += idade
    if sexo == 'masculino':
        if idade > maiorIdade:
            maiorIdade = idade
            NomeMaiorIdade = nome
    elif sexo == 'feminino':
        if idade < 20:
            QuantMulher += 1
print('-='*20)
print('A MÉDIA DE IDADE do grupo é: {:.1f}'.format(somaIdade/4))
print('O nome do HOMEM MAIS VELHO é: {}. Ele tem {} anos.'.format(NomeMaiorIdade, maiorIdade))
print('A quantidade de mulheres que têm MENOS DE 20 ANOS é: {}'.format(QuantMulher))

print('-='*20)