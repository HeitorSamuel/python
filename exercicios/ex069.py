contIdade = 0
contHomem = 0
contMulherMenor = 0
while True:
    print('-'*30)
    print(f'{'CADASTRE UMA PESSOA':^30}')
    print('-'*30)
    idade = int(input('Digite a Idade: ').strip())
    sexo = str(input('Digite o Sexo: [M/F] ').strip().upper()[0])
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite o Sexo: [M/F] ').strip().upper()[0])
    print('-'*30)
    if idade > 18:
        contIdade += 1
    if sexo == 'M':
        contHomem += 1
    if sexo == 'F':
        if idade < 20:
            contMulherMenor += 1
    continuar = str(input('Você quer continuar? [S/N] ').strip().upper()[0])
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Você quer continuar? [S/N] ').strip().upper()[0])
    if continuar == 'N':
        break

print(f'{' FIM DO PROGRAMA ':=^30}')
print(f'Total de pessoas com mais de 18 anos: {contIdade}')
print(f'Ao todo, temos {contHomem} homens cadastrados!')
print(f'E temos {contMulherMenor} mulheres com menos de 20 anos')