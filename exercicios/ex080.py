valores = []

for c in range(0, 5):
    num = int(input('Digite um número: ').strip())
    if c == 0:
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        if num < valores[0]:
            valores.insert(0, num)
            print('Adicionado na posição 0 da lista...')
        elif num > valores[0] and num < valores[-1]:
            valores.insert(1, num)
            print('Adicionado na posição 1 da lista...')
        elif num > valores[-1]:
            valores.append(num)
            print('Adicionado ao final da lista...')
print('-='* 30)
print(f"Os valores digitados em ordem foram {valores}")