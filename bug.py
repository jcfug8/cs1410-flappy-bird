import pygame, random, math

class Bug:

    def __init__(self, width, height):
        self.right_limit = width
        self.left_limit = width/ 3
        self.screen_height = height - 30
        self.x = width
        self.y = random.randint(0, height)
        self.dx = 7
        self.dy = 7
        self.scale = 3.5
        self.imgIndex = 0
        self.sheet_back = pygame.image.load("images/bug-sprite-back.png")
        self.sprite_size = self.sheet_back.get_size()
        self.sprite_locations_back = [(0,0), (171,0)]
        self.resize_sprites()
        self.animate_back = self.save_animation(self.sheet_back, self.sprite_locations_back)


    def resize_sprites(self):
        self.sheet_back = pygame.transform.scale(self.sheet_back, (int(self.sprite_size[0]/self.scale), int(self.sprite_size[1]/self.scale)))
        for index, location in enumerate(self.sprite_locations_back):
            self.sprite_locations_back[index] = int(location[0] / self.scale), int(location[1] / self.scale)


    def save_animation(self, sheet, locations):
        images = []
        for i in range(len(locations)):
            images.append(sheet.subsurface(locations[i],(int(85/self.scale),int(80/self.scale))))
        return images

    def paint(self, surface):
        surface.blit(self.animate_back[self.imgIndex],(self.x,self.y))
        self.imgIndex += 1
        if self.imgIndex > len(self.sprite_locations_back) - 1:
            self.imgIndex = 0

    def move(self):
        self.right_limit -= 5
        self.left_limit -= 5
        choices = ["up", "down", "left", "right"]
        directions = []
        directions.append(random.choice(choices))
        choices.remove(directions[0])
        if "right" in choices:
            choices.remove("right")
        directions.append(random.choice(choices))
        for direction in directions:
            if direction == "up" and self.y >= 0:
                self.y -= self.dy
            elif direction == "down" and  self.y <= self.screen_height:
                self.y += self.dy
            elif direction == "left" and self.x >= self.left_limit:
                self.x -= self.dx
            elif direction == "right" and self.x <= self.right_limit:
                self.x += self.dx

    def collision_check(self, bird):
        x = self.x + 25
        y = self.y + 2
        radius = 20
        if math.sqrt((x - bird.x)**2 + (y - bird.y)**2) <= radius + bird.radius:
            return True
        return False
