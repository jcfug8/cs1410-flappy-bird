import pygame
import math
class Bird:
    pygame.mixer.pre_init(44100, -16, 2, 4096) #frequency, size, channels, buffersize
    pygame.init() #turn all of pygame on.
    def __init__(self, width, height):
        self.sound_up = pygame.mixer.Sound('Robot_blip.wav')
        self.sound_down = pygame.mixer.Sound('Robot_blip.wav')
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
                #self.sound_up.play()
                self.y -= 15
        if self.y + self.radius <= self.screen_height:
            if pygame.K_DOWN in newkeys:
                #self.sound_down.play()
                self.y += 5
            self.x += 0
        else:
            self.y = self.screen_height - self.radius
            self.x += 0
        self.y += 5

    def collision_check(self, bar_x, bottom_of_TW, top_of_BW, bar_width):
        if self.x + self.radius >= bar_x and self.x - self.radius <= bar_x + bar_width:
            if self.y >= top_of_BW + 1 or self.y <= bottom_of_TW - 1:
                print("Wall")
            #if self.y + self.radius * .75 >= top_of_BW or self.y - self.radius * .75 <= bottom_of_TW:
        if math.sqrt((self.x - (bar_x + bar_width))**2 + (self.y - bottom_of_TW)**2) <= self.radius or math.sqrt((self.x - (bar_x + bar_width))**2 + (self.y - top_of_BW)**2) <= self.radius:
            print("Front Corner")
        if math.sqrt((self.x - (bar_x + bar_width))**2 + (self.y - bottom_of_TW)**2) <= self.radius or math.sqrt((self.x - (bar_x + bar_width))**2 + (self.y - top_of_BW)**2) <= self.radius:
            print("Back Corner")
