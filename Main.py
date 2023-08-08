# /* Main.py
import pygame
from random import randint
from Menu import Menu
from Dungeon import Dungeon
from Game import Huncho_Derivative


pygame.init()


# Checkers class takes in scream parameter which initialized several class
# attributes, including window, running and FPS.
class Checkers:
    def __init__(self, window, setting):
        # Window represents the game window
        self.window = window
        # Running is a boolean that determines whether the game is still running
        self.running = True
        # FPS is a Pygame clock that limits the game to a certain frame rate
        self.FPS = pygame.time.Clock()
        # Setting is a class that contains multiple variables that can have multiple states
        # These settings can change how the checkers game plays out.
        self.setting = setting

    # The draw method takes in the dungeon parameter and draws the game board
    def _draw(self, dungeon, checkJump):
        dungeon.draw(self.window, checkJump)
        pygame.display.update()

    # The main method is the main game loop
    # Taking in window width and height and the constant board size to calculate tile width and height
    def main(self, window_width, window_height):
        checkJump = self.setting.forced_jump
        checkedJump = 0
        dungeon_size = 8
        tile_width, tile_height = window_width // dungeon_size, window_height // dungeon_size
        # Initialize both board and game with appropriate class
        dungeon = Dungeon(tile_width, tile_height, dungeon_size, checkJump)
        huncho_Derivative = Huncho_Derivative()
        print (self.setting.forced_jump)
        # While loop runs as long as self.running is true
        while self.running:
            # Checks for random and sets the move rule accordingly
            if self.setting.forced_jump == 'random' and checkedJump == 0:
                x = randint(0, 1)
                if x == 0:
                    checkJump = 'yes'
                    print("Heads")
                if x == 1:
                    checkJump = 'no'
                    print("Tails")
            # Check for any viable jumps in the board
            if checkedJump == 0:
                huncho_Derivative.check_jump(dungeon, checkJump)
                checkedJump = 1

            # Loop through events.
            for self.event in pygame.event.get():
                # If event is pyGame.quit, exit game by setting self.running to False
                if self.event.type == pygame.QUIT:
                    self.running = False

                # Check if user has clicked on a tile
                if not huncho_Derivative.is_game_over(dungeon):
                    if self.event.type == pygame.MOUSEBUTTONDOWN:
                        if dungeon.handle_click(self.event.pos, checkJump):
                            checkedJump = 0
                # If the game is over display game over message and exit loop
                else:
                    huncho_Derivative.message(self.setting)
                    self.running = False

            self._draw(dungeon, checkJump)
            self.FPS.tick(60)


#  __name__ == "__main__"
# Ensures that the code isn't run when imported as module
if __name__ == "__main__":
    # set the window dimensions to 640 x 640
    window_size = (640, 640)
    # Create a display screen captioned "Checkers"
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Checkers")
    # sets up the display screen and starts the game loop
    menu = Menu(window_size, screen)

    while menu.loop:
        menu.draw()
        if menu.loop:
            checkers = Checkers(screen, menu.setting)
            checkers.main(window_size[0], window_size[1])
