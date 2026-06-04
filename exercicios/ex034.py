salario = float(input('Digite o seu salário: '))
if salario > 1250:
    print('Você ganhou um aumento de 10%, o que corresponde a R${}!\nO seu novo salário é de R${:.2f}!'.format((salario*0.1), (salario*1.1)))
else:
    print('Você ganhou um aumento de 15%, o que correspode a R${}\nO seu novo salário é de R${:.2f}!'.format((salario*0.15), (salario*1.15)))