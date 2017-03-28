import barrier, closing_barrier, moving_barrier, random

class Barriers:

    def __init__(self, height, width):
        self.screen_width = width
        self.screen_height = height
        self.barrier_types = [barrier.Barrier(width, height),
                              closing_barrier.ClosingBarrier(width, height),
                              moving_barrier.MovingBarrier(width, height)]
        self.barriers = [random.choice(self.barrier_types)]
        self.num_barriers = len(self.barriers)
        self.openings = 200
        self.add_barriers = True

    def move(self):
        for barrier in self.barriers:
            barrier.move()
        self.add_barrier(self.barriers[len(self.barriers)-1])
        if self.barriers[0].x < -50:
            self.barriers.pop(0)
        if self.barriers[0].x <= 0 and len(self.barriers) >= 8 and self.add_barriers == True :
            self.add_barriers = False
            return "bugs"
        if len(self.barriers) == 5:
            self.add_barriers = True

    def paint(self, surface):
        for barrier in self.barriers:
            barrier.paint(surface)

    def add_barrier(self, last):
        if self.screen_width - last.x > 100 and self.add_barriers == True:
            self.barrier_types = [barrier.Barrier(self.screen_width, self.screen_height, last.last, self.openings),
                                  closing_barrier.ClosingBarrier(self.screen_width, self.screen_height, last.last, self.openings),
                                  moving_barrier.MovingBarrier(self.screen_width, self.screen_height, last.last, self.openings)]
            if self.num_barriers % 5 == 0:
                self.openings -= 10
            self.barriers.append(random.choice(self.barrier_types))
            self.num_barriers += 1


    def collision_check(self, bird):
        for barrier in self.barriers:
            if bird.collision_check(barrier.x, barrier.bottom_of_TW, barrier.top_of_BW, barrier.width):
                return True
        return False

    def reset(self):
        self.barriers = [barrier.Barrier(self.screen_width, self.screen_height)]
        self.opening = 150
