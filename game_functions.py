import sys
import pygame

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """
    реагирует на нажатие клавиш
    """
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
    """
    Обрабатывает нажатие клавиш и мыши
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """
    Обновляет изображения на экране и отображает новый экран
    """
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


def get_number_aliens_x(ai_settings, alien_width):
    """
    вычисляет кличество нло в ряду
    """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """
    определяет количесво рядов нло
    """
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """
    создает нло и размещает в ряду
    """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """
    создает флот нло
    """
    # создание нло и вычисление их количества в ряду
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # создание флота нло
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # создание и размещение нло в ряду
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
