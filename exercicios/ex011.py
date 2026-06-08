cores = {
    'limpar':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'roxo':'\033[35m'
}

larg = float(input('{}Digite a largura da parede em metros(m):{} '.format(cores['verde'], cores['limpar'])))
alt = float(input('{}Digite a altura da parede em metros(m):{} '.format(cores['roxo'], cores['limpar'])))
area = larg*alt
print('A área da parede vale: {}{}m²{} \ne a quantidade de tinta necessária para pintá-la é de: {}{:.0f}L{}'.format(cores['amarelo'], area, cores['limpar'], cores['vermelho'], area/2, cores['limpar']))