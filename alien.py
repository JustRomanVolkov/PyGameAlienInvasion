import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """
    класс нло
    """
    def __init__(self, ai_game):
        """
        ининциализирует нло и задает его начальную позицию
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # загрузка изображения нло и атрибута rect
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # каждый новый нло появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной позиции нло
        self.x = float(self.rect.x)

    def check_edges(self):
        """
        возвращает True, если нло у края.
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """
        перемещает нло вправо или влево
        """
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
