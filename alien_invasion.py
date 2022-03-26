import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # создание корабля
    ship = Ship(ai_settings, screen)

    # запуск основного цикла игры
    while True:
        # отслеживание событий клавиатуры и мыши
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
