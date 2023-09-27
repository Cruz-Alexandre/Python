# Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.#

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mexer.music.play()
pygame.event.wait()

# Não tem mp3 no computador, mas esse seria os comandos para tocar uma música.#