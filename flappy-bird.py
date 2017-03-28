import pygame, math, random
import game_mouse, barriers, bird, menu, score, background, bug
import main_menu, end_menu, pause_menu, instruction_menu, displayscoresmenu
# Starter code for PyGame applications
pygame.mixer.pre_init(44100, -16, 2, 4096) #frequency, size, channels, buffersize
pygame.init() #turn all of pygame on.

class Flappy_Bird(game_mouse.Game):
    def __init__(self, width, height, fps):
        pygame.font.init()
        game_mouse.Game.__init__(self, "Flappy Bird",
                                 width,
                                 height,
                                 fps)
        self.state = 'Main Menu'
        self.main_menu =  main_menu.Main_Menu(width, height)
        self.end_menu = end_menu.End_Menu(width, height)
        self.pause = pause_menu.Pause_Menu(width, height)
        self.barriers = barriers.Barriers(height, width)
        self.bird = bird.Bird(width, height)
        self.score = score.Score(width, height)
        self.scores_menu = displayscoresmenu.ScoresMenu(width, height)
        self.background = background.Background(height, width)
        self.music = { "state" : "",
                       "songs" : ["sounds/palm-beach.wav",
                                  "sounds/chubby-cat.wav",
                                  "sounds/the-awakening.wav"],
                        "current" : ""}
        self.instruction_menu = instruction_menu.InstructionMenu(width, height)
        self.bugs = []
        self.bug = bug.Bug
        return

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        x = mouse_position[0]
        y = mouse_position[1]
        self.play_music()
        self.background.move_clouds()
        self.sound_level(keys)
        if self.state == "Main Menu":
            self.state = self.main_menu.user_interact(keys, newkeys)
        elif self.state == "Instructions":
            self.bird.move_logic(newkeys, keys)
            self.state = self.instruction_menu.user_interact(keys, newkeys)
            if pygame.K_RETURN in keys:
                self.bird.reset()
        elif self.state == "Play" or self.state == "Play Again":
            if self.barriers.move() == "bugs":
                for i in range(random.randrange(1,5)):
                    self.bugs.append(self.bug(self.width, self.height))
            self.score.updateScore(self.bird.move_logic(newkeys, keys))
            for bug in self.bugs:
                bug.move()

                if bug.x < 0 or bug.collision_check(self.bird):
                    self.bugs.remove(bug)
                    self.score.updateScore(False, True)
            if self.barriers.collision_check(self.bird):
                self.barriers.reset()
                self.bird.reset()
                if len(self.bugs) > 0:
                    self.bugs = []
                scorePos = self.score.checkNewHighScore()
                if scorePos < 5:
                    self.state = "NewHighScore"
                else:
                    self.score.reset()
                    self.state = "End Menu"
            if pygame.K_p in newkeys:
                self.state = "Pause Menu"
        elif self.state == "NewHighScore":
            self.state = self.score.HSmenu(keys, newkeys)
        elif self.state == "End Menu":
            self.state = self.end_menu.user_interact(keys, newkeys)
        elif self.state == "High Scores":
            self.state = self.scores_menu.user_interact(keys, newkeys)
        elif self.state == "Pause Menu":
            self.state = self.pause.user_interact(keys, newkeys)
            if self.state == "Main Menu":
                if len(self.bugs) > 0:
                    self.bugs = []
                if self.score.score > 0:
                    self.score.reset()
                self.barriers.reset()

        return

    def paint(self, surface):
        surface.fill((178, 233, 255))
        self.background.paint_back_clouds(surface)
        if self.state == "Main Menu":
            self.main_menu.paint(surface)
        if self.state == "Instructions":
            self.instruction_menu.paint(surface)
            self.bird.paint(surface)
        elif self.state == "Play" or self.state == "Play Again":
            self.barriers.paint(surface)
            self.background.paint_ground(surface)
            self.bird.paint(surface)
            for bug in self.bugs:
                bug.paint(surface)
            self.score.paint(surface, "play")
        elif self.state == "Pause Menu":
            self.barriers.paint(surface)
            self.background.paint_ground(surface)
            self.bird.paint(surface)
            self.score.paint(surface, "play")
            self.pause.paint(surface)
        elif self.state == "NewHighScore":
            self.score.paint(surface, "newHSmenu")
        elif self.state == "End Menu":
            self.end_menu.paint(surface)
        elif self.state == "High Scores":
            self.scores_menu.paint(surface)
        self.background.paint_front_clouds(surface)
        return

    def play_music(self):
        if self.music["state"] != self.state:
            if self.state in ["Play", "Play Again", "Pause Menu"] and self.music["current"] != self.music["songs"][1]:
                self.music["current"] = self.music["songs"][1]
                pygame.mixer.music.load(self.music["songs"][1])
                pygame.mixer.music.play(-1)
            elif self.state == "End Menu" and self.music["current"] != self.music["songs"][2]:
                self.music["current"] = self.music["songs"][2]
                pygame.mixer.music.load(self.music["songs"][2])
                pygame.mixer.music.play(-1)
            elif self.music["current"] != self.music["songs"][0]:
                self.music["current"] = self.music["songs"][0]
                pygame.mixer.music.load(self.music["songs"][0])
                pygame.mixer.music.play(-1)
            self.music["state"] = self.state

    def sound_level(self, keys):
        if pygame.K_PLUS in keys or pygame.K_EQUALS in keys:
            volume = pygame.mixer.music.get_volume()
            if volume < 1:
                volume += .05
                pygame.mixer.music.set_volume(volume)
        elif pygame.K_MINUS in keys:
            volume = pygame.mixer.music.get_volume()
            if volume > 0:
                volume -= .05
                pygame.mixer.music.set_volume(volume)

def main():
    screen_width = 800
    screen_height = 500
    frames_per_second = 10
    game = Flappy_Bird(screen_width, screen_height, frames_per_second)
    game.main_loop()
    return

if __name__ == "__main__":
    main()
