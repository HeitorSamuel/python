cores = {
    'limpar':'\033[m',
    'texto':'\033[7;31;40m',
}

import pygame

pygame.init()

pygame.mixer.music.load('exercicios/lonely.mp3')
pygame.mixer.music.play()

input('{}Pressione Enter para sair...{}'.format(cores['texto'], cores['limpar']))
