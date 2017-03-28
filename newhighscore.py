import menu, pygame

class NewHighScore(menu.Menu):

    def __init__(self, width, height):
        menu.Menu.__init__(self, width, height)
        self.name = "NewHighScore"
        self.text = ["High Score! What is Your Name?", "     "]
        self.positions = self.set_positions()
        self.user_name = ""

    def user_interact(self, keys, newkeys):
        self.positions = self.set_positions()
        self.move_arrows(newkeys)
        self.user_name = self.text[1]
        for key in newkeys:
            if key == pygame.K_BACKSPACE:
                self.user_name = self.user_name[0:len(self.user_name) - 1]
            elif key == pygame.K_RETURN:
                break
            elif key <= 127:
                self.user_name += chr(key)
                self.user_name = self.user_name.strip(" ")
        self.text[1] = self.user_name.title()
        return self.select_option(newkeys)
