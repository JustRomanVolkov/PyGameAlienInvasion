class GameStats():
    """
    отслеживает статистику игры
    """
    def __init__(self, ai_settings):
        """
        инициализирует  статистику
        """
        self.ai_settings = ai_settings
        self.reset_stats()

        # игра запускается при активном состоянии
        self.game_active = False

    def reset_stats(self):
        """
        инициализирует статистику меняющуюся в ходе игры
        """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0

