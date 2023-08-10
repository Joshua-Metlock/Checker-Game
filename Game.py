# /* Game.py
# Game class is created to check for winner
class Huncho_Derivative:
    def __init__(self):  # initializes the winner variable to None
        self.winner = None

    # checks if both colors still has a piece
    def check_piece(self, dungeon):  # checks over each tile on the board and if it is occupied
        red_piece = 0
        black_piece = 0
        for y in range(dungeon.dungeon_size):
            for x in range(dungeon.dungeon_size):
                tile = dungeon.get_tile_from_pos((x, y))
                if tile.occupying_piece != None:
                    if tile.occupying_piece.color == "red":
                        red_piece += 1  # adds to red_piece count if color is red
                    else:
                        black_piece += 1  # adds to black_piece count if color is black
        return red_piece, black_piece

    # checks to see if the game is over and declare the winner
    # returns true if the game is over and false if not
    def is_game_over(self, dungeon):
        red_piece, black_piece = self.check_piece(dungeon)
        # if one side has no pieces declare a winner
        if red_piece == 0 or black_piece == 0:
            self.winner = "red" if red_piece > black_piece else "black"
            return True
        else:
            return False

    def check_jump(self, dungeon, jumpSetting):
        piece = None
        for tile in dungeon.tile_list:
            if tile.occupying_piece != None:
                piece = tile.occupying_piece
                if len(piece.valid_jumps()) != 0 and dungeon.turn == piece.color:
                    dungeon.is_jump = True
                    break
                else:
                    dungeon.is_jump = False
        if dungeon.is_jump and jumpSetting == 'yes':
            dungeon.selected_piece = piece
            dungeon.handle_click(piece.pos, jumpSetting)
        return dungeon.is_jump

    def message(self, setting):
        if self.winner == setting.player1.col:
            if (self.winner == 'red' and not setting.red_AI) or (self.winner == 'black' and not setting.black_AI):
                print(f"{setting.player1.nickName} WINS!!!")
                setting.player1.calculate_experince(True)
            else:
                print(f"{self.winner.upper()} AI WINS!")
            if (self.winner != 'red' and not setting.red_AI) or (self.winner != 'black' and not setting.black_AI):
                print(f"{setting.player2.nickName} LOSES!!!")
                setting.player2.calculate_experince(False)
            else:
                print(f"{setting.player2.col.upper()} AI LOSES")
        else:
            if (self.winner == 'red' and not setting.red_AI) or (self.winner == 'black' and not setting.black_AI):
                print(f"{setting.player2.nickName} WINS!!!")
                setting.player2.calculate_experince(True)
            else:
                print(f"{self.winner.upper()} AI WINS!")
            if (self.winner != 'red' and not setting.red_AI) or (self.winner != 'black' and not setting.black_AI):
                print(f"{setting.player1.nickName} LOSES!!!")
                setting.player1.calculate_experince(False)
            else:
                print(f"{setting.player1.col.upper()} AI LOSES")
        print(f"{self.winner} Wins!!! ")
