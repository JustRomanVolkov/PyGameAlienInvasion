import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """
    класс нло
    """
    def __init__(self, ai_settings, screen):
        """
        ининциализирует нло и задает его начальную позицию
        """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # загрузка изображения нло и атребута rect
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # каждый новый нло появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной позиции нло
        self.x = float(self.rect.x)

    def blitme(self):
        """
        выводит пришельца в текущем положении
        """
        self.screen.blit(self.image, self.rect)


    def update(self):
        """
        перемещает нло вправо
        """
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x

