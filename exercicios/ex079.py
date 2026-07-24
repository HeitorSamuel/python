valores = []
while True:
    valor = int(input('Digite um valor: ').strip())
    if valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    perg = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    while perg not in 'S' and perg not in 'N':
        perg = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    if perg == 'N':
        break
valores.sort()
print('-='*30)
print(f'Você digitou os valores {valores}')
print()
