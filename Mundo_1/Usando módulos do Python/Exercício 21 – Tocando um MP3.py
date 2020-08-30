"""
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

Biblioteca pygame -- 1.9.6 (pip install pygame)

Não deu certo :/

"""

import pygame

pygame.init()
pygame.mixer.music.load("ex21.mp3")
pygame.mixer.music.play
