import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """класс управления пулями корабля"""

    def __init__(self, ai_game):
        """создает объект пули в текущей позиции корабля"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # создание пули в позиции (0, 0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # позиция пули хранится в вещественном формате
        self.y = float(self.rect.y)

    def update(self):
        """перемещает пулю вверх по экрану"""
        # обновление позиции в вещественном формате
        self.y -= self.settings.bullet_speed
        # обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        """вывод пули"""
        pygame.draw.rect(self.screen, self.color, self.rect)
