import barrier


class MovingBarrier(barrier.Barrier):

    def move(self):
        self.x -= self.dx
        if self.bottom_of_TW < self.base_pos_top - self.opening//2 or self.bottom_of_TW < 0:
            self.dy *= -1
        if self.top_of_BW > self.base_pos_bottom + self.opening//2 or self.top_of_BW > self.screen_height :
            self.dy *= -1
        self.bottom_of_TW += self.dy
        self.top_of_BW += self.dy

    def set_color(self):
        return (40, 40, 40)
