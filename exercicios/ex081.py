valores = []
cont = 0
while True:
    num = int(input('Digite um valor: ').strip())
    cont += 1
    valores.append(num)
    perg  = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    while perg not in "N" and perg not in "S":
        perg  = str(input('Valor inválido! Quer continuar? [S/N] ').strip().upper()[0])
    if perg == 'N':
        break
print('-='*30)
valores.sort(reverse=True)
print(f"Você digitou {cont} elementos.")
print(f"Os valores em ordem decrescente são {valores}")
if 5 in valores:
    print("O valor 5 faz parte da  lista!")
else:
    print("O valor 5 não foi encontrado na lista!")