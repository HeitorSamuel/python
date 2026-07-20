valores = []
while True:
    valor = int(input('Digite um valor: ').strip())
    for i, v in enumerate(valores):
        valores.append(valor)
        if v == valor:
            print('Valor duplicado! Não vou adicionar...')
        else:
            valores.append(valor)
            print('Valor adicionado com sucesso!')
    '''perg = str(input('Quer continuar? [S/N]').strip().upper())
    while 'S' not in perg and 'N' not in perg:
        perg = str(input('Quer continuar? [S/N]').strip().upper())
    if perg == 'N':
        break'''
print(f'Você digitou os valores {valores}')
