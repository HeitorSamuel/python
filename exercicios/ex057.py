sexo = str(input('Digite o seu sexo: [M/F] ')).upper().strip()[0]

while sexo != 'M' and sexo != 'F':
    sexo = str(input('OPÇÃO INVÁLIDA! Por favor digite novamente: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))