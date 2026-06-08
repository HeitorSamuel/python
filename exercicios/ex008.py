cores = {
    'limpar':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'azul':'\033[34m',
    'roxo':'\033[35m',
    'ciano':'\033[36m'
}

medida = float(input('Digite um valor em {}metros(m){}: '.format(cores['azul'], cores['limpar'])))
km = medida/1000
hm = medida/100
dam = medida/10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('O seu valor em {}quilometro é {}km{}, \no seu valor em {}hectômetro é {}hm{}, \no seu valor em {}decâmetro é {}dam{}, \no seu valor em {}decímetro é {:.0f}dm{}, \no seu valor em {}centímetros é {:.0f}cm{}, \no seu valor em {}milímetros é {:.0f}mm{}.'.format(cores['amarelo'], km, cores['limpar'], cores['roxo'], hm, cores['limpar'], cores['ciano'], dam, cores['limpar'], cores['verde'], dm, cores['limpar'], cores['vermelho'], cm, cores['limpar'], cores['azul'], mm, cores['limpar']))