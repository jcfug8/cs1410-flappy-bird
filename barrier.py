import random, pygame

class Barrier():

    def __init__(self, width, height, last = 150, opening = 150):
        self.screen_width = width
        self.screen_height = height
        self.color = self.set_color()
        self.opening = opening
        self.difference = 150
        self.x = width
        self.width = 20
        self.dy = self.set_dy()
        self.dx = 5
        self.opening_limit_1 = self.set_opening_limit_1(last)
        self.opening_limit_2 = self.set_opening_limit_2(last)
        self.bottom_of_TW = random.randint(self.opening_limit_1 , self.opening_limit_2)
        self.top_of_BW = self.bottom_of_TW + self.opening
        self.last = self.bottom_of_TW
        self.base_pos_top = self.bottom_of_TW
        self.base_pos_bottom = self.top_of_BW

    def paint(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, 0, self.width, self.bottom_of_TW))
        pygame.draw.rect(surface, self.color, (self.x, self.top_of_BW, self.width, self.screen_height ))

    def set_color(self):
        return (100, 100, 100)

    def set_dy(self):
        temp = 0
        while temp == 0:
            temp = random.randint(-3,3)
        return temp

    def set_opening_limit_1(self, last):
        if last < self.difference:
            return 0
        elif last + self.opening > self.screen_height:
            return self.screen_height - self.difference - self.opening
        else:
            return last - self.difference
    def set_opening_limit_2(self, last):
        if last + self.opening + self.difference >= self.screen_height - 30:
            return self.screen_height - self.opening
        else:
            return self.difference + last

    def move(self):
        self.x -= self.dx
