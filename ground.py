import pygame

class Ground:

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.height = 30
        self.x = screen_height - self.height

    def paint(self, surface):
        pygame.draw.rect(surface, (50, 165, 46), (0, self.x, self.screen_width, self.height ))
