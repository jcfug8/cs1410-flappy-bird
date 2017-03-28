import pygame

class Menu_Arrow:

    def __init__(self, position):
        self.position = position
        self.x1, self.y1, self.text_width = position
        self.x1 -= 20
        self.y1 += 10
        self.x2 = self.x1 + self.text_width + 36
        self.y2 = self.y1

    def paint(self, surface):
        pygame.draw.polygon(surface, (0,0,0), [(self.x1, self.y1), (self.x1 + 10, self.y1 + 15), (self.x1, self.y1 + 30)])
        pygame.draw.polygon(surface, (0,0,0), [(self.x2, self.y2), (self.x2 - 10, self.y2 + 15), (self.x2, self.y2 + 30)])

    def move(self, position):
        self.x1, self.y1, self.text_width = position
        self.x1 -= 20
        self.y1 += 10
        self.x2 = self.x1 + self.text_width + 36
        self.y2 = self.y1
