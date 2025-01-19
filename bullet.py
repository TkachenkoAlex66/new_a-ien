import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self, ai_game):
        """Создает объект снарядов в текущей позиции корабля"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # Создание снаряда позиции 0,0 и назначение правильной позиции
        # self.rect = pygame.Rect(0,0,3,30)
        self.rect = pygame.Rect(0,0, self.settings.bullet_weidth, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        # Позиция снаряда хранится в вещественном формате
        self.y = float(self.rect.y)
    def update(self):
        """Перемещает снаряд вверх по экрану"""
        # Обновлении позиции снаряда в вещественном форм ате
        self.y -= self.settings.bullet_speed
        # Обновление позиции треугольника
        self.rect.y = self.y
    def draw_bullet(self):
        """Вывод снаряда на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)



