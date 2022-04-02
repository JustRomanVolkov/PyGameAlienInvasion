class Settings():
    """Класс для храниния настроек игры"""
    
    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        # настройки корабля
        self.ship_limit = 3
        # параметры пули
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3
        # настройки нло
        self.fleet_drop_speed = 10
        # темп ускорения игры
        self.speed_up_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        инициализирует настройки меняющиеся в ходе игры
        """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction = 1 <<< вправо, -1 <<< влево
        self.fleet_direction = 1

        # награда за убийство нло
        self.alien_points = 50

    def increase_speed(self):
        """
        увеличивает настройки скорости
        """
        self.ship_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale
