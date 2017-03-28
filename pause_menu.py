import menu

class Pause_Menu(menu.Menu):

    def __init__(self, width, height):

        menu.Menu.__init__(self, width, height)
        self.name = "Pause Menu"
        self.text = ["Paused", "Play", "Main Menu"]
        self.positions = self.set_positions()
