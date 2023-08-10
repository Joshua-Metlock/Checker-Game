import pygame
from Player import Player


class Setting():
    def __init__(self):
        # Toggable Settings
        self.forced_jump = 'yes'
        self.best_of = 1
        self.red_AI = False
        self.black_AI = False
        # Players
        self.player1 = Player('Player 1', 'Black')
        self.player2 = Player('Player 2', 'Red')
