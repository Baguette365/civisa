import pygame #import pygame
import src.map.map
class Game:
    def __init__(self):
        pygame.init() #initialize pygame

        self.map = src.map.map.Map()

        self.map.CreateMap()

    def CreateWindow(self, sizeX,sizeY):
        self.window = pygame.display.set_mode((sizeX,sizeY)) #set the window size

        icon = pygame.image.load("assets/icon.png")

        pygame.display.set_icon(icon)

        pygame.display.set_caption("Beyond the Horizon")

    def MainLoop(self):
        running=True #set the MainLoop

        while running:
            #self.window.blit(self.map.grass, (0,0))

            pygame.display.flip()#refresh graphics

            for event in pygame.event.get(): #keep all inputs

                if event.type==pygame.QUIT: #if the player want quit the game

                    running=False # break the mainloop

            pygame.time.Clock()

        pygame.quit() #quit the game



























