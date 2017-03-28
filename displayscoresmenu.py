import menu, pygame

class ScoresMenu(menu.Menu):

    def __init__(self, width, height):
        menu.Menu.__init__(self, width, height, 50)
        self.name = "High Scores"
        self.text = self.getHighScores()
        self.positions = self.set_positions()
        self.choice = len(self.positions) - 1

    def getHighScores(self):
        scores = ["High Scores", ""]
        try:
            with open("phlappy_bird_scores.txt", "r+") as fin:
                for line in fin:
                    (name, score) = line.split()
                    scores.append((name + " " + score))
        except OSError:
            with open("phlappy_bird_scores.txt", "w") as fout:
                for line in range(5):
                    fout.write("N/A 0\n")
            with open("phlappy_bird_scores.txt", "r+") as fin:
                for line in fin:
                    (name, score) = line.split()
                    scores.append((name + " " + score))
        scores.append("")
        scores.append("Main Menu")
        return scores

    def move_arrows(self, newkeys):
        self.text = self.getHighScores()
        self.positions = self.set_positions()
        self.arrows.move(self.positions[self.choice])
