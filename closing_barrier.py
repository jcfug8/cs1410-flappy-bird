import barrier


class ClosingBarrier(barrier.Barrier):

    def __init__(self, width, height, last = 150, opening = 150):

        barrier.Barrier.__init__(self, width, height, last, opening)

    def move(self):
        self.x -= self.dx
        if self.bottom_of_TW >= self.top_of_BW - self.opening//2 or self.top_of_BW - self.bottom_of_TW < 35:
            self.dy *= -1
        if self.top_of_BW > self.base_pos_bottom or self.top_of_BW < self.base_pos_top:
            self.dy *= -1
        self.bottom_of_TW += self.dy
        self.top_of_BW -= self.dy

    def set_color(self):
        return (140, 140, 140)
