while True:
    print('-='*25)
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-='*25)
    if valor < 0:
        break
    cont = 1
    while cont <= 10:
        print(f'{valor} x {cont} = {valor*cont}')
        cont += 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')