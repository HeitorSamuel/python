cores = {
    'limpar':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[32m',
    'azul':'\033[34m',
    'roxo':'\033[35m',
    'ciano':'\033[36m'
}

salario = float(input('{}Digite o seu salário:{} '.format(cores['ciano'], cores['limpar'])))
if salario > 1250:
    print('{}Você ganhou um aumento de 10%,{} {}o que corresponde a{} {}R${}!{}\n{}O seu novo salário é de{} {}R${:.2f}!{}'.format(cores['amarelo'], cores['limpar'], cores['roxo'], cores['limpar'], cores['azul'], (salario*0.1), cores['limpar'], cores['roxo'], cores['limpar'], cores['verde'], (salario*1.1), cores['limpar']))
else:
    print('{}Você ganhou um aumento de 15%,{} {}o que correspode a{} {}R${}!{}\n{}O seu novo salário é de{} {}R${:.2f}!{}'.format(cores['amarelo'], cores['limpar'], cores['roxo'], cores['limpar'], cores['azul'], (salario*0.15), cores['limpar'], cores['roxo'], cores['limpar'], cores['verde'], (salario*1.15), cores['limpar']))