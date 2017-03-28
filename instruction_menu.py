import menu

class InstructionMenu(menu.Menu):

    def __init__(self, width, height):
        menu.Menu.__init__(self, width, height, 25)
        self.name = "Instructions"
        self.text = ["How To Play", "Use the arrows to move around, but if you hit",
                                    "the sides of the screen or a barrier it is",
                                    "game over. Your score will increase when you eat",
                                    "bugs and slowly as the games goes on. Don't forget",
                                    "that hitting the buttons to flap will make your score",
                                    "increase slower. If you wish to change the music's",
                                    "volume, hit the + or - buttons and P to pause.", "",
                     "Main Menu"]
        self.positions = self.set_positions()
        self.choice = len(self.positions) - 1

    def move_arrows(self, newkeys):
        self.arrows.move(self.positions[self.choice])
