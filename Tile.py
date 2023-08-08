# /* Tile.py
import pygame


class Tile:
    def __init__(self, x, y, tile_width, tile_height):
        # x and y are the coordinates of the tile (array)
        self.x = x
        self.y = y
        self.pos = (x, y)
        # tile width and height are measured in pixels
        self.tile_width = tile_width
        self.tile_height = tile_height
        # absolute x and y are the coordinates of the tile (pixel)
        self.abs_x = x * tile_width
        self.abs_y = y * tile_height
        self.abs_pos = (self.abs_x, self.abs_y)
        # sets the color of tile to light if even and dark if odd
        self.color = 'light' if (x + y) % 2 == 0 else 'dark'
        self.draw_color = (220, 189, 194) if self.color == 'light' else (53, 53, 53)
        self.highlight_color = (100, 249, 83) if self.color == 'light' else (0, 228, 10)
        # occupying_piece is set None by default, but can have a piece added to it
        self.occupying_piece = None
        self.coord = self.get_coord()
        self.highlight = False
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            self.tile_width,
            self.tile_height
        )

    # return coordinates as classic chess notation, with lettered columns, and numbered rows.
    def get_coord(self):
        columns = 'abcdefgh'
        return columns[self.x] + str(self.y +1)

    # draws the tile on the screen using pygame.draw.rect
    def draw(self, display):
        # if the tile is highlighted use self.highlight_color as the fill color
        # else use the tile's normal color
        if self.highlight:
            pygame.draw.rect(display, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(display, self.draw_color, self.rect)

        # if there's a piece on the tile, blit the image in the center of the tile
        if self.occupying_piece is not None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.occupying_piece.img, centering_rect.topleft)

