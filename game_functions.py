import sys
import pygame

def check_events():
    """ Обрабатывает нажатие клафиш и мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            sys.exit()
            
def update_screen(ai_settings, screen, ship):
    """Обновляет изображения на экране и отображает новый экран."""
    # перерисовка экрана
    screen.fill(ai_settings.bg_color)
    ship.blitme()
        
    # отображение последнего прорисованного экрана
    pygame.display.flip()
