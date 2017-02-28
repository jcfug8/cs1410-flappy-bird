import random

class Barrier():

    def __init__(self, x_start, y_height):
        self.x = x_start
        self.bottom_of_TW = random.randrage(0,y_height+1)
        self.top_ofBW = self.bottom_of_TW + 50
        self.top_wall = TopWall(0, self.bottom_of_TW)
        self.bottom_wall = BottomWall(self.bottom_of_TW, y_height)

    def move(self, speed):
        self.x -= speed
