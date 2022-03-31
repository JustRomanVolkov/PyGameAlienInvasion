import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf


def run_game():
    # инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # создание экземпляра хранения игровой статистики
    stats = GameStats(ai_settings)

    # создание корабля, группы пуль и группы нло
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # создает флот нло
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # запуск основного цикла игры
    while True:
        # отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
