import sys
import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        # переместить корабль вправо
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # переместить корабль влево
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # создание пули и включение ее в группу
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # переместить корабль вправо
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # переместить корабль вправо
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """ Обрабатывает нажатие клавиш и мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """Обновляет изображения на экране и отображает новый экран."""
    # перерисовка экрана
    screen.fill(ai_settings.bg_color)
    # все пули выводятся позади изображения корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
        
    # отображение последнего прорисованного экрана
    pygame.display.flip()


def update_bullets(bullets):
    """
    обновляет позиции пуль и удаляет старые
    """
    bullets.update()

    # удаление пуль за экраном
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
