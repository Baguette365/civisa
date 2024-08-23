#import the main class of the game
from src.core.game import *
#instantiate the game
game = Game()
#initialize the game window
game.CreateWindow(600,800)
#create the mainloop
game.MainLoop()