import pygame, newhighscore
class Score:

    def __init__(self, width, height):
        self.score = 0
        self.font = pygame.font.SysFont("Helvetica", 20)
        self.textsurface = self.font.render("Score: " + str(self.score), True, (0,0,0))
        self.scores = self.getHighScores()
        self.newHSmenu = newhighscore.NewHighScore(width, height)
        self.scorePos = 6

    def paint(self, surface, state):
        if state == "play":
            surface.blit(self.textsurface, (10,10))
        elif state == "newHSmenu":
            self.newHSmenu.paint(surface)

    def updateScore(self, move, bug = False):
        if move:
            self.score -= 10
        else:
            self.score += 10
        if bug:
            self.score += 100
        self.textsurface = self.font.render("Score: " + str(self.score), True, (0,0,0))

    def getHighScores(self):
        scores = []
        try:
            with open("phlappy_bird_scores.txt", "r+") as fin:
                for line in fin:
                    (name, score) = line.split()
                    scores.append((name, int(score)))
        except OSError:
            with open("phlappy_bird_scores.txt", "w") as fout:
                for line in range(5):
                    fout.write("N/A 0\n")
            with open("phlappy_bird_scores.txt", "r+") as fin:
                for line in fin:
                    (name, score) = line.split()
                    scores.append((name, int(score)))
        return scores

    def setHighScores(self):
        with open("phlappy_bird_scores.txt", "w") as fout:
            for line in range(5):
                name, score = self.scores[line]
                fout.write(name + " " + str(score) + "\n" )

    def checkNewHighScore(self):
        newindex = 0
        for index, scoreInfo in enumerate(self.scores):
            name, score = scoreInfo
            if self.score < score:
                newindex = index + 1
        self.scorePos = newindex
        return newindex

    def HSmenu(self, keys, newkeys):
        temp = self.newHSmenu.user_interact(keys, newkeys)
        if temp == "NewHighScore":
            return "NewHighScore"
        else:
            self.scores.insert(self.scorePos, (temp, self.score))
            self.scores.pop(5)
            self.setHighScores()
            self.reset()
            return "Main Menu"

    def reset(self):
        self.score = 0
