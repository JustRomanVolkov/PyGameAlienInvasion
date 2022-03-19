# библиотеки для установки Pygame
# sudo apt-get install python3.v*-dev mercurial
# sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev 

# для звуков установить
# sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
# sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcode-dev
# sudo apt-get install python-numpy

# установка pygame
# pip install --user hg+http://bitbucket.org/pygame/pygame

# для тестиустановки в консоли
# $ python3
# import pygame

import sys 
import pygame
from settings import Settings

def run_game():
    # инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
  
    # запуск основного цикла игры
    while True:
        # отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            # перерисовка экрана
            screen.fill(ai_settings.bg_color)
            if event.type == pygame.QUIT():
            sys.exit()
        
    # отображение последнего прорисованного экрана
    pygame.display.flip()
    
run_game()
