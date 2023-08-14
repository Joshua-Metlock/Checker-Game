import pygame
from Setting import Setting
from Button import Button


# pygame.init()

class Menu:
    # Logo
    logo_img = pygame.image.load(f'images/Huncho Derivative.png')
    logo = Button(0, 0, logo_img, 1.3)
    # Button Images
    options_img = pygame.image.load(f'images/Options.png')
    player_img = pygame.image.load(f'images/Player.png')
    play_img = pygame.image.load(f'images/Play.png')
    forcedJump_img = pygame.image.load(f'images/Forced-Jump.png')
    return_img = pygame.image.load(f'images/Return.png')
    player1_img = pygame.image.load(f'images/Player 1.png')
    player2_img = pygame.image.load(f'images/Player 2.png')
    reset_img = pygame.image.load(f'images/Reset.png')
    swap_img = pygame.image.load(f'images/Swap.png')
    black_ai_img = pygame.image.load(f'images/Black AI.png')
    red_ai_img = pygame.image.load(f'images/Red AI.png')

    # Buttons
    options_button = Button(425, 400, options_img, .4)
    player_button = Button(225, 400, player_img, .4)
    play_button = Button(25, 400, play_img, .4)
    forcedJump_button = Button(225, 200, forcedJump_img, .4)
    return_button = Button(425, 200, return_img, .4)
    player1_button = Button(25, 150, player1_img, .2)
    player2_button = Button(25, 400, player2_img, .2)
    reset1_button = Button(150, 150, reset_img, .2)
    reset2_button = Button(150, 400, reset_img, .2)
    swap_button = Button(250, 250, swap_img, .3)
    black_ai_button = Button(25, 5, black_ai_img,  .4)
    red_ai_button = Button(225, 5, red_ai_img, .4)

    def __init__(self, window_size, screen):
        # State
        self.state = 'main'
        # Calculations
        self.window_size = window_size
        self.screen = screen
        # Determining if to exit to Checker game or desktop
        self.running = True
        self.loop = True
        # Game Variables
        self.setting = Setting()
        # PlayerList
        self.playerList = []
        # Fonts
        self.font = pygame.font.SysFont("arialblack", 48)
        self.font1 = pygame.font.SysFont("arialblack", 20)
        self.text_col = (255, 0, 0)  # Red
        self.text_act_col = (255, 155, 0)
        self.text_pas_col = (5, 5, 5)

    # Adds text to the menu, separate from a button
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    # Draws the menu and updates the menu
    def draw(self):
        self.running = True
        color1 = self.text_pas_col
        color2 = self.text_pas_col
        active1 = False
        active2 = False
        while self.running:
            # While in the main menu
            if self.state == 'main':
                self.screen.fill((48, 150, 220))  # Purple
                # Draws the logo onto the screen
                Menu.logo.draw(self.screen)
                # Draws the play button and if the play button is pressed
                # The menu is closed down and the checker game begins
                if Menu.play_button.draw(self.screen):
                    self.running = False
                # Draws the player button and if the player button is pressed
                # Go to the player menu
                if Menu.player_button.draw(self.screen):
                    self.state = 'player'
                # Draws the options button and if the menu button is pressed
                # Go the options menu
                if Menu.options_button.draw(self.screen):
                    self.state = 'options'
            # While in the options menu
            if self.state == 'options':
                # Fill in the screen with purple
                self.screen.fill((48, 150, 220))
                #
                self.draw_text(self.setting.forced_jump, self.font, self.text_col, 225, 400)
                self.draw_text(str(self.setting.red_AI), self.font, self.text_col, 25, 500)
                self.draw_text(str(self.setting.black_AI), self.font, self.text_col, 25, 550)
                if Menu.red_ai_button.draw(self.screen):
                    self.setting.red_AI = not self.setting.red_AI
                if Menu.black_ai_button.draw(self.screen):
                    self.setting.black_AI = not self.setting.black_AI
                if Menu.forcedJump_button.draw(self.screen):
                    if self.setting.forced_jump == 'yes':
                        self.setting.forced_jump = 'no'
                    elif self.setting.forced_jump == 'no':
                        self.setting.forced_jump = 'random'
                    else:
                        self.setting.forced_jump = 'yes'
                if Menu.return_button.draw(self.screen):
                    self.state = 'main'
            # While in the player menu
            if self.state == 'player':
                self.screen.fill((48, 150, 220))
                if Menu.return_button.draw(self.screen):
                    self.state = 'main'
                    active1 = False
                    active2 = False
                if Menu.swap_button.draw(self.screen):
                    temp_holder = self.setting.player1.col
                    self.setting.player1.col = self.setting.player2.col
                    self.setting.player2.col = temp_holder
                # Code dealing with Player1 Button
                # Which allows the user to change Nickname
                player1text = str(self.setting.player1)
                if active1:
                    color1 = self.text_act_col
                else:
                    color1 = self.text_pas_col
                self.draw_text(player1text, self.font1, color1, 25, 100)
                if Menu.player1_button.draw(self.screen):
                    active1 = not active1
                    active2 = False
                    # print('push')
                if Menu.reset1_button.draw(self.screen):
                    self.setting.player1.reset()
                # Code dealing with Player2 Button
                # Which allows the user to change Nickname
                player2text = str(self.setting.player2)
                if active2:
                    color2 = self.text_act_col
                else:
                    color2 = self.text_pas_col
                self.draw_text(player2text, self.font1, color2, 25, 500)
                if Menu.player2_button.draw(self.screen):
                    active1 = False
                    active2 = not active2
                    # print('push')
                if Menu.reset2_button.draw(self.screen):
                    self.setting.player2.reset()
            for event in pygame.event.get():
                # Changing Player1's Nickname
                if event.type == pygame.KEYDOWN and active1:
                    if event.key == pygame.K_BACKSPACE:
                        self.setting.player1.nickName = self.setting.player1.nickName[:-1]
                    else:
                        self.setting.player1.nickName += event.unicode

                # Changing Player2's Nickname
                if event.type == pygame.KEYDOWN and active2:
                    if event.key == pygame.K_BACKSPACE:
                        self.setting.player2.nickName = self.setting.player2.nickName[:-1]
                    else:
                        self.setting.player2.nickName += event.unicode

                # Exits program without going to game
                if event.type == pygame.QUIT:
                    self.running = False
                    self.loop = False
            pygame.display.update()
