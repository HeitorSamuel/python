num =  quant = soma = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    quant += 1
    soma += num
print(f'Foram digitados {quant} valores, e a soma deles foi de {soma}!')