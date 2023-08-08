# /* Piece.py
import pygame


# the piece class is the parent class for all checker pieces in play
# as such, it contains the common attributes and methods shared by all peaces on the board
# valid moves and jumps are not defined within the Piece class, and are instead defined within the pawn and king class
# as those are unique to their respective peaces.
class Piece:
    def __init__(self, x, y, color, dungeon):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.dungeon = dungeon
        self.color = color

    # the move method intakes the a tile object that represents the new position
    def _move(self, tile, jumpSetting):
        move = False
        for i in self.dungeon.tile_list:
            i.highlight = False
        # ordinary move/s
        # checks to see if the move is valid and if it's just an ordinary move
        # because it's an ordinary move, just update the position
        if tile in self.valid_moves() and (not self.dungeon.is_jump or jumpSetting != 'yes'):
            prev_tile = self.dungeon.get_tile_from_pos(self.pos)
            self.pos, self.x, self.y = tile.pos, tile.x, tile.y
            prev_tile.occupying_piece = None
            tile.occupying_piece = self
            self.dungeon.selected_piece = None
            self.has_moved = True
            # Pawn promotion
            # checks to see if the piece is a pawn and that it's reached either end of the play area by moving
            # if so, promote piece to king
            if self.notation == 'p':
                if self.y == 0 or self.y == 7:
                    from King import King
                    tile.occupying_piece = King(
                        self.x, self.y, self.color, self.dungeon
                    )
            return True
        # jump move/s
        # checks to see if the move is valid and if it's a jump move
        # because it's an jump move, update position and remove piece jumped over
        elif self.dungeon.is_jump:
            for move in self.valid_jumps():
                if tile in move:
                    prev_tile = self.dungeon.get_tile_from_pos(self.pos)
                    jumped_piece = move[-1]
                    self.pos, self.x, self.y = tile.pos, tile.x, tile.y
                    prev_tile.occupying_piece = None
                    jumped_piece.occupying_piece = None
                    tile.occupying_piece = self
                    self.dungeon.selected_piece = None
                    self.has_moved = True
                    # Pawn promotion
                    if self.notation == 'p':
                        if self.y == 0 or self.y == 7:
                            from King import King
                            tile.occupying_piece = King(
                                self.x, self.y, self.color, self.dungeon
                            )
                    return True
        else:
            # if the move is not valid, return false and do not move the piece and
            self.dungeon.selected_piece = None
            return False
