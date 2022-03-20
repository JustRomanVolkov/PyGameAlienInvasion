import sys
import pygame

def check_events():
    """ Обрабатывает нажатие клафиш и мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            sys.exit()
