valor = 0
while True:
    print('-='*25)
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-='*25)
    cont = 1
    if valor < 0:
        break
    while cont <= 10:
        produto = valor * cont
        print(f'{valor} x {cont} = {produto}')
        cont += 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')