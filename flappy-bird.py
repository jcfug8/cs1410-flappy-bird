import pygame
import math
import game_mouse
import barrier
import bird

# Starter code for PyGame applications

class PygameStarter(game_mouse.Game):

    def __init__(self, width, height, fps):

        game_mouse.Game.__init__(self, "Pygame Starter",
                                 width,
                                 height,
                                 fps)
        self.barriers = [barrier.Barrier(width, height)]
        self.bird = bird.Bird(width, height)
        return

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        x = mouse_position[0]
        y = mouse_position[1]

        if pygame.K_a in newkeys:
            print("a key pressed")

        if 1 in newbuttons:
            print("button clicked")

        newest_bar = self.barrier_loop()

        self.bird.move_logic(keys, newkeys)
        if self.barriers[len(self.barriers) - 1].x < self.width - 80:
            self.barriers.append(barrier.Barrier(self.width, self.height, newest_bar.bottom_of_TW))
        return

    def paint(self, surface):
        surface.fill((255,255,255))
        for bar in self.barriers:
            bar.paint(surface)
        self.bird.paint(surface)
        return

    def barrier_loop(self):
        destroy_barrier = False
        for bar in self.barriers:
            bar.move()
            if bar.x + bar.width <= 0:
                destroy_barrier = True
            self.bird.collision_check(bar.x, bar.bottom_of_TW, bar.top_of_BW, bar.width)
        if destroy_barrier == True:
            self.barriers.pop(0)
        return bar

def main():
    screen_width = 600
    screen_height = 300
    frames_per_second = 10
    game = PygameStarter(screen_width, screen_height, frames_per_second)
    game.main_loop()
    return

if __name__ == "__main__":
    main()
