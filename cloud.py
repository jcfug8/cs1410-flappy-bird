import pygame, random

class Cloud:

    def __init__(self, screen_width, screen_height, cloud, front_back):
        self.front_back = front_back
        self.cloud = cloud
        self.width = random.randint(90,150)
        self.height = random.randint(60, 120)
        self.cloud = pygame.transform.scale(cloud, (self.width, self.height))
        self.y = random.randint(0, screen_height - 200)
        self.x = screen_width
        self.dx = random.randint(1,10)

    def move(self):
        self.x -= self.dx
        if self.x < 0 - self.width:
            return True
        return False


    def paint(self, surface):
        surface.blit(self.cloud, (self.x, self.y))
