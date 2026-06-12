valCasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
valAnos = int(input('Digite em quantos anos você vai pagar a casa: '))
prestMensal = valCasa/(valAnos*12)

if prestMensal <= salario * (30/100):
    print('O seu empréstimo foi APROVADO! \nO valor de cada prestação do empréstimo é de R${:.2f}'.format(prestMensal))
else:
    print('O seu empréstimo foi NEGADO! \nA prestação mensal excede os 30% do seu salário, o que seria: R${:.2f}, sendo o limite de R${:.2f}!'.format(prestMensal, (salario * (30/100))))