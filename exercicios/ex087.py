matriz = []
linha = []
somaPares = 0
somaTerColun = 0
maiorSegLinha = 0
for l in range(0, 3):
    for c in range(0, 3):
        item = int(input(f'Digite um valor para [{l}, {c}]: '))
        if l == 1:
            if c == 1: 
                maiorSegLinha = item
            else:
                if item > maiorSegLinha:
                    maiorSegLinha = item
        linha.append(item)
        if len(linha) == 3:
            matriz.append(linha[:])
            linha.clear()
print('-='*30)
for linhas in matriz:
    somaTerColun += linhas[2]
    for num in linhas:
        if num % 2 == 0:
            somaPares += num
        print(f'[{num:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {somaPares}.')
print(f'A soma dos valores da terceira coluna é {somaTerColun}.')
print(f'O maior valor da segunda linha é {maiorSegLinha}.')


