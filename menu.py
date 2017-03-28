import pygame, menu_arrow

class Menu:

    def __init__(self, width, height, y= 100):
        self.y = y
        self.name = "menu"
        self.screen_width = width
        self.screen_height = height
        self.small_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.large_font = pygame.font.SysFont('Comic Sans MS', 45)
        self.text = ["Menu Class", "Option1", "Option2"]
        self.positions = self.set_positions()
        self.arrows = menu_arrow.Menu_Arrow(self.positions[0])
        self.choice = 1

    def set_positions(self):
        position = []
        y = self.y
        for text in self.text:
            x, height, width = self.center(text, self.text.index(text))
            position.append((x, y, width))
            y += height
        return position

    def paint(self, surface):
        for i, text in enumerate(self.text):
            x, y, width = self.positions[i]
            if i == 0:
                textsurface = self.large_font.render(text, False, (0, 0, 0))
            else:
                textsurface = self.small_font.render(text, False, (0, 0, 0))
            surface.blit(textsurface, (x, y))
        self.arrows.paint(surface)


    def center(self, text, index):
        if index == 0:
            width, height = self.large_font.size(text)
        else:
            width, height = self.small_font.size(text)
        x = self.screen_width//2 - width//2
        return x, height, width

    def user_interact(self, keys, newkeys):
        self.move_arrows(newkeys)
        return self.select_option(newkeys)

    def select_option(self, newkeys):
        if pygame.K_RETURN in newkeys:
            return self.text[self.choice]
        else:
            return self.name
        return self.name

    def move_arrows(self, newkeys):
        if pygame.K_UP in newkeys:
            if self.choice == 1:
                self.choice = len(self.text) - 1
            else:
                self.choice -= 1
        if pygame.K_DOWN in newkeys:
            if self.choice == len(self.text) - 1:
                self.choice = 1
            else:
                self.choice += 1
        self.arrows.move(self.positions[self.choice])
