import pygame

class Bird:

    def __init__(self, width, height):
        self.screen_width = width
        self.screen_height = height
        self.x = width // 2
        self.y = height // 2
        self.color = ((0,0,0))
        self.radius = 10

    def paint(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move_logic(self, keys, newkeys):

        if self.y - self.radius > 0:
            if pygame.K_UP in newkeys:
                self.y -= 15
        if self.y + self.radius <= self.screen_height:
            if pygame.K_DOWN in newkeys:
                self.y += 5
            self.x += 0
        else:
            self.y = self.screen_height - self.radius
            self.x += 0
        self.y += 5
