sexo = str(input('Digite o seu sexo: [M/F] ')).upper().strip()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('OPÇÃO INVÁLIDA! Por favor digite novamente! ')).upper().strip()
print('Sexo {} registrado com sucesso!'.format(sexo))