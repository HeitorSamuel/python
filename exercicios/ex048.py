s = quantidade = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
        quantidade += 1
print('A SOMA dos {} valores solicitados é {}'.format(quantidade, s))