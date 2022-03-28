import sys
import pygame

from bullet import Bullet
from alien import Alien


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
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Обновляет изображения на экране и отображает новый экран."""
    # перерисовка экрана
    screen.fill(ai_settings.bg_color)
    # все пули выводятся позади изображения корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
        
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


def fire_bullet(ai_settings, screen, ship, bullets):
    """
    выпускает пулю, если максимум еще не достигнут
    """
    # создание пули и включениее ее в группу
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens):
    """
    создает флот нло
    """
    # зодание нло и вычисление их количества в ряду
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    availible_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(availible_space_x/(2*alien_width))

    # создание первого ряда нло
    for alien_number in range(number_aliens_x):
        # создание и размещение нло в ряду
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
