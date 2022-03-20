import pygame

class Ship():
    
    def __init__(self, screen):
        """Инициализирует корабль и задает его начальную позицию """
        self.screen = screen
        
        # загрузка изображения корабля и получение прямоугольника 
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get.rect()
        self.screen_rect = screen.get_rect()
        
        # каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.sсreen_rect.centerx
        self.rect.bottom = self.sсreen_rect.bottom
        
    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
        
