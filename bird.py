import pygame, math, random
class Bird:

    def __init__(self, width, height):
        #sprite attributes
        self.scale = 4
        self.imgIndex = 0
        self.sheet_forward = pygame.image.load("images/bird-sprite.png")
        self.sheet_back = pygame.image.load("images/bird-sprite-back.png")
        self.sprite_size = self.sheet_forward.get_size()
        self.sprite_locations_forward = [(0,0), (182, 0), (364, 0), (546, 0), (728, 0),
                                 (0,171), (182, 171), (364, 171), (546, 171), (728, 171),
                                 (0,342), (182, 342), (364, 342), (546, 342)]
        self.sprite_locations_back = [(728, 0),(546, 0),(364, 0),(182, 0),(0,0),
                                 (728, 171),(546, 171),(364, 171),(182, 171),(0,171),
                                 (728,342),(546, 342),(364, 342),(182, 342)]
        self.resize_sprites()
        self.animate_back = self.save_animation(self.sheet_back, self.sprite_locations_back)
        self.animate_forward = self.save_animation(self.sheet_forward, self.sprite_locations_forward)
        #sound attributes
        #other attributes
        self.screen_width = width
        self.screen_height = height
        self.x = width // 2
        self.y = height // 2
        self.radius = 13
        self.color = ((0,0,0))
        self.direction = "forward"

    def reset(self):
        self.x = self.screen_width // 2
        self.y = self.screen_height // 2
        self.direction = "forward"

    def paint(self, surface):
        if self.direction == "forward":
            surface.blit(self.animate_forward[self.imgIndex],(self.x-26,self.y-25))
        else:
            surface.blit(self.animate_back[self.imgIndex],(self.x-26,self.y-25))
        if self.imgIndex == 4 and random.randint(1,10) > 1 or self.y + self.radius + 20 >= self.screen_height:
            pass
        else:
            self.imgIndex += 1
        if self.imgIndex > len(self.sprite_locations_forward) - 1:
            self.imgIndex = 0

    def resize_sprites(self):
        self.sheet_forward = pygame.transform.scale(self.sheet_forward, (int(self.sprite_size[0]/self.scale), int(self.sprite_size[1]/self.scale)))
        self.sheet_back = pygame.transform.scale(self.sheet_back, (int(self.sprite_size[0]/self.scale), int(self.sprite_size[1]/self.scale)))
        for index, location in enumerate(self.sprite_locations_forward):
            self.sprite_locations_forward[index] = int(location[0] / self.scale), int(location[1] / self.scale)
        for index, location in enumerate(self.sprite_locations_back):
            self.sprite_locations_back[index] = int(location[0] / self.scale), int(location[1] / self.scale)

    def save_animation(self, sheet, locations):
        images = []
        for i in range(len(locations)):
            images.append(sheet.subsurface(locations[i],(int(182/self.scale),int(172/self.scale))))
        return images

    def move_logic(self, newkeys, keys):
        flap = False
        self.y += 5
        if pygame.K_LEFT in keys:
            self.x -= 4
            self.direction = "backward"
            if random.randint(1,10) == 10:
                flap = True

        if pygame.K_RIGHT in keys:
            self.x += 3
            self.direction = "forward"
            if random.randint(1,10) == 10:
                flap = True

        if self.y - self.radius > 0:
            if pygame.K_UP in newkeys:
                # self.sound_up.play()
                self.y -= 15
                flap = True

        if self.y + self.radius + 20 <= self.screen_height:
            if pygame.K_DOWN in newkeys:
                # self.sound_down.play()
                self.y += 7
                flap = True
        else:
            self.y = self.screen_height - self.radius - 20
            self.x -= 5

        return flap

    def collision_check(self, bar_x, bottom_of_TW, top_of_BW, bar_width):
        if self.x - self.radius < 0 or self.x + self.radius > self.screen_width:
            return True

        if self.x + self.radius >= bar_x and self.x - self.radius <= bar_x + bar_width:
            if self.y >= top_of_BW + 1 or self.y <= bottom_of_TW - 1:

                return True
            #if self.y + self.radius * .75 >= top_of_BW or self.y - self.radius * .75 <= bottom_of_TW:
        if math.sqrt((self.x - (bar_x + bar_width))**2 + (self.y - bottom_of_TW)**2) <= self.radius or math.sqrt((self.x - (bar_x + bar_width))**2 + (self.y - top_of_BW)**2) <= self.radius:

            return True
        if math.sqrt((self.x - (bar_x + bar_width))**2 + (self.y - bottom_of_TW)**2) <= self.radius or math.sqrt((self.x - (bar_x + bar_width))**2 + (self.y - top_of_BW)**2) <= self.radius:

            return True
        return False
