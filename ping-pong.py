import pygame


pygame.init()

class Game:
    def __init__(self, name):
        self.scene_width = 800
        self.scene_height = 600

        self.SCENE = pygame.display.set_mode([self.scene_width, self.scene_height])
        pygame.display.set_caption(name)
        




game = Game('pong')

