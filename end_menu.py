import menu

class End_Menu(menu.Menu):

    def __init__(self, width, height):
        menu.Menu.__init__(self, width, height)
        self.name = "End Menu"
        self.text = ["Game Over :(", "Play Again", "Main Menu"]
        self.positions = self.set_positions()
