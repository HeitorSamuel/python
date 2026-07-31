matriz = [
    
]
linha = []
for l in range(0, 3):
    for c in range(0, 3):
        item = int(input(f'Digite um valor para [{l}, {c}]: '))
        linha.append(item)
        if len(linha) > 2:
            matriz.append(linha[:])
            linha.clear()
for linhas in matriz:
    for num in linhas:
        print(f'[ {num} ]', end='')