class Settings():
    """Класс для храниния настроек игры"""
    
    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        # настройки корабля
        self.ship_speed_factor = 1.5
        # параметры пули
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3
        # настройки нло
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 <<< вправо, -1 <<< влево
        self.fleet_direction = 1


