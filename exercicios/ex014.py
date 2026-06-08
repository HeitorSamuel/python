cores = {
    'limpar':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[32m',
    'roxo':'\033[35m',
    'ciano':'\033[36m'
}

tempC = float(input('{}Digite a temperatura em °C:{} '.format(cores['ciano'], cores['limpar'])))
tempF = (tempC * 1.8) + 32
print('{}A temperatura de{} {}{}°C{} {}corresponde a {}{}°F{}'.format(cores['amarelo'], cores['limpar'], cores['verde'], tempC, cores['limpar'], cores['amarelo'], cores['limpar'], cores['roxo'], tempF, cores['limpar']))