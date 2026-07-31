matriz = []
linha = []
for l in range(0, 3):
    for c in range(0, 3):
        item = int(input(f'Digite um valor para [{l}, {c}]: '))
        linha.append(item)
        if len(linha) == 3:
            matriz.append(linha[:])
            linha.clear()
print('-='*30)
for linhas in matriz:
    for num in linhas:
        print(f'[{num:^5}]', end='')
    print()