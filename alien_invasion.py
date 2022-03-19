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

def run_game():
  # инициализирует игру и создает объект экрана
  pygame.init()
  screen = pygame.display.set_mode((1200, 800))
  pygame.display.set_caption("Alien Invasion")
  
  # запуск основного цикла игры
  while True:
    # отслеживание событий клавиатуры и мыши
    for event in pygame.event.get():
      if event.type == pygame.QUIT():
        sys.exit()
        
    # отображение последнего прорисованного экрана
    pygame.display.flip()
    
run_game()
