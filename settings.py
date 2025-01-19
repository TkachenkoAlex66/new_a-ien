class Settings:
    game_name = 'Alien'
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (200,200,200)
        self.ship_speed = 1.5
        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_weidth = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5


