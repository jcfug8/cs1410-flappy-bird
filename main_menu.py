import menu

class Main_Menu(menu.Menu):

    def __init__(self, width, height):
        menu.Menu.__init__(self, width, height)
        self.name = "Main Menu"
        self.text = ["Welcome to Phlappy Bird", "Play", "High Scores", "Instructions"]
        self.positions = self.set_positions()
