valores = []
pares = []
impares = []

for n in range(1, 8):
    num = int(input(f'Digite o {n}º valor: '))
    if num % 2 == 0:
        pares.append(num)     
    elif num % 2 != 0:
        impares.append(num)
valores.append(pares)
valores.append(impares)
pares.sort()
impares.sort()
print('-='*30)
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')