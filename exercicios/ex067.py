valor = 0
cont = 1

while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    while cont <= 10:
        produto = valor * cont
        print(f'{valor} x {cont} = {produto}')
        cont += 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')