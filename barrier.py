import random
import pygame

class Barrier():

    def __init__(self, width, height, last = 50):
        self.opening = 100
        self.screen_width = width
        self.screen_height = height
        self.difference = 150
        self.x = width
        self.width = 20
        self.color = (100,100,100)
        self.dx = 5
        if last < self.difference:
            print(1)
            self.opening_limit_1 = 0
        elif last + self.opening > self.screen_height:
            print(2)
            self.opening_limit_1 = self.screen_height - self.difference - self.opening
        else:
            print(3)
            self.opening_limit_1 = last - self.difference

        if self.opening_limit_1 + self.opening + self.difference >= self.screen_height:
            self.opening_limit_2 = self.screen_height - self.opening
        else:
            self.opening_limit_2 = self.difference + self.opening_limit_1
        self.bottom_of_TW = random.randint(self.opening_limit_1 , self.opening_limit_2)
        self.top_of_BW = self.bottom_of_TW + self.opening
        self.last = self.bottom_of_TW
        print("limit1 ", self.opening_limit_1)
        print("limit2 ", self.opening_limit_2, " x ", self.bottom_of_TW)
        if self.opening_limit_2 > self.screen_height:
            print("warning!")
    def paint(self, surface):

        pygame.draw.rect(surface, self.color, (self.x, 0, self.width, self.bottom_of_TW))
        pygame.draw.rect(surface, self.color, (self.x, self.top_of_BW, self.width, self.screen_height ))
    def move(self):
        self.x -= self.dx
