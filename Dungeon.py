# /* Dungeon.py
import pygame
from Tile import Tile
from Pawn import Pawn
from random import choice


class Dungeon:
    def __init__(self, tile_width, tile_height, dungeon_size, setting):
        # dimension of the playing area and which piece is selected
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.dungeon_size = dungeon_size
        self.selected_piece = None
        # the settings that were set up in the menu
        self.setting = setting

        self.turn = "black"
        self.is_jump = False

        # the initial board state
        self.config = [
            ['.', 'bp', '.', 'bp', '.', 'bp', '.', 'bp'],
            ['bp', '.', 'bp', '.', 'bp', '.', 'bp', '.'],
            ['.', 'bp', '.', 'bp', '.', 'bp', '.', 'bp'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['rp', '.', 'rp', '.', 'rp', '.', 'rp', '.'],
            ['.', 'rp', '.', 'rp', '.', 'rp', '.', 'rp'],
            ['rp', '.', 'rp', '.', 'rp', '.', 'rp', '.']
        ]
        # create the dungeon and sets it up
        self.tile_list = self._generate_tiles()
        self._setup()

    # generates a list of tiles using tile width and height along dungeon size
    def _generate_tiles(self):
        output = []
        for y in range(self.dungeon_size):
            for x in range(self.dungeon_size):
                output.append(
                    Tile(x, y, self.tile_width, self.tile_height)
                )
        return output

    # return the tile at given position
    def get_tile_from_pos(self, pos):
        for tile in self.tile_list:
            if (tile.x, tile.y) == (pos[0], pos[1]):
                return tile

    # Sets up the initial board state
    def _setup(self):
        # Iterate through the self.config list
        for y_ind, row in enumerate(self.config):
            for x_ind, x in enumerate(row):
                tile = self.get_tile_from_pos((x_ind, y_ind))
                # Set up the occupying_piece attribute to a pawn if config tile isn't empty.
                if x != '':
                    if x[-1] == 'p':
                        color = 'red' if x[0] == 'r' else 'black'
                        tile.occupying_piece = Pawn(x_ind, y_ind, color, self)

    # Handle_click is a method that intakes pos, which represents the pixel coordinates that were clicked
    def handle_click(self, pos, checkjump):
        # Extracts x and y coordinates from pos
        x, y = pos[0], pos[1]
        # If coordinates are larger than board size, calculate what tile was clicked based on tile width and height
        if x >= self.dungeon_size or y >= self.dungeon_size:
            x = x // self.tile_width
            y = y // self.tile_height
        # Retrieve tile from coordinates
        clicked_tile = self.get_tile_from_pos((x, y))
        """
        print(clicked_tile.pos)
        """
        # Checks to see if the player has not selected a piece
        if self.selected_piece is None:
            #  Checks to see if the tile selected has anything
            if clicked_tile.occupying_piece is not None:
                # Checks to see if piece selected is the same color as the player
                if clicked_tile.occupying_piece.color == self.turn:
                    # Sets selected piece equal to piece clicked on if all conditions satisfied
                    self.selected_piece = clicked_tile.occupying_piece
                    # The board state has not changed
                    return False
        # If player does have a selected piece, attempt to move it to clicked tile
        elif self.selected_piece._move(clicked_tile, checkjump):
            if not self.is_jump:
                # Turns the turn to red player if black last held a turn
                # Else it's black's turn
                self.turn = 'red' if self.turn == 'black' else 'black'
                return True
            else:
                # Check to see if the Piece object has any more jumps
                # If there are no more valid jumps, change turn
                if len(clicked_tile.occupying_piece.valid_jumps()) == 0:
                    self.turn = 'red' if self.turn == 'black' else 'black'
                    return True
        # If the clicked tile does have a Pawn Object to it
        # And it belongs to current player's turn
        # Selected piece changes to the newly clicked piece
        elif clicked_tile.occupying_piece is not None:
            if clicked_tile.occupying_piece.color == self.turn:
                self.selected_piece = clicked_tile.occupying_piece

    # Handle_AI deals with moving pieces during the AI's turn.
    def handle_AI(self, checkjump):
        # If the AI has not selected a piece.
        if self.selected_piece is None:
            # Find all valid pieces to click on
            valid_pieces = []
            for y in range(self.dungeon_size):
                for x in range(self.dungeon_size):
                    tile = self.get_tile_from_pos((x, y))
                    if tile.occupying_piece != None:
                        if tile.occupying_piece.color == self.turn:
                            valid_pieces.append(tile.occupying_piece)
            if len(valid_pieces) > 0:
                self.selected_piece = choice(valid_pieces)
                return False
        else:
            # Code for handling AI Jumping
            if len(self.selected_piece.valid_jumps()) > 0:
                clicked_tile = choice(self.selected_piece.valid_jumps())
                clicked_tile = choice(clicked_tile)
                """
                for x in clicked_tile:
                    print(x.pos)
                """
                if self.selected_piece._move(clicked_tile, checkjump):
                    print("CJ")
                    if len(clicked_tile.occupying_piece.valid_jumps()) == 0:
                        self.turn = 'red' if self.turn == 'black' else 'black'
                        return True
            elif not self.is_jump and len(self.selected_piece.valid_moves()) > 0:
                clicked_tile = choice(self.selected_piece.valid_moves())
                if self.selected_piece._move(clicked_tile, checkjump):
                    self.turn = 'red' if self.turn == 'black' else 'black'
                    return True
            else:
                self.selected_piece = None
                return False
    # The draw method is used to update the display after handle_click method is called
    def draw(self, display, checkJump):
        # If a piece is currently selected, highlight the tile it is on and all valid moves/jumps
        if self.selected_piece is not None:
            self.get_tile_from_pos(self.selected_piece.pos).highlight = True
            if not self.is_jump or checkJump != 'yes':
                for tile in self.selected_piece.valid_moves():
                    tile.highlight = True
            if self.is_jump or checkJump != 'yes':
                for tile in self.selected_piece.valid_jumps():
                    tile[0].highlight = True

        for tile in self.tile_list:
            tile.draw(display)
