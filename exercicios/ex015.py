cores = {
    'limpar':'\033[m',
    'amarelo':'\033[1;33m',
    'verde':'\033[4;32m',
    'vermelho':'\033[31m',
    'azul':'\033[4;34m'
}

dia = int(input('{}Quantos dias o seu carro ficou alugado?{} '.format(cores['azul'], cores['limpar'])))
kmPerc = int(input('{}Quantos km você percorreu com o carro alugado?{} '.format(cores['verde'], cores['limpar'])))
diaCalc = 60 * dia
kmCalc = 0.15 * kmPerc
print('{}O preço total a pagar pelo aluguel do carro é de:{} {}R${:.2f}{}'.format(cores['vermelho'], cores['limpar'], cores['amarelo'], diaCalc+kmCalc, cores['limpar']))