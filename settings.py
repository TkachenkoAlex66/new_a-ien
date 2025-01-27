class Settings:
    game_name = 'Alien'
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 1200
        self.bg_color = (200,200,200)
        self.ship_speed = 1.5
        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_weidth = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5
        self.alien_speed = 1.0
        self.fleet_drop_speed = 0
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1


