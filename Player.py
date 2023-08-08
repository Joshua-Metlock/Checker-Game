# /* Player.py


class Player(object):
    # by default, a fraction is 0/1
    def __init__(self, nick="Nick", color="X"):
        self.nickName = nick
        self.col = color
        self.exp = 0
        self.consecutive_games = 0
        self.games_played = 0
        self.points = 0

    # getter for Nickname
    @property
    def nickName(self):
        return self._nickName

    # setter for Nickname
    @nickName.setter
    def nickName(self, value):
        self._nickName = value

    # getter for Level
    @property
    def exp(self):
        return self._exp

    # setter for Level
    @exp.setter
    def exp(self, value):
        self._exp = value

    # getter for Symbol
    @property
    def col(self):
        return self._col

    # setter for Symbol
    @col.setter
    def col(self, value):
        self._col = value

    def calculate_experince(self, win=True):
        # if won, increase by one.
        # if lose, decrease to zero.
        if win:
            self.consecutive_games += 1
            self.points += 1
        else:
            self.consecutive_games = 0
        self.games_played += 1
        # match level to games consecutively won
        match self.consecutive_games:
            case 0:
                self.exp = 0
            case 3:
                self.exp = 1
            case 5:
                self.exp = 2
            case 7:
                self.exp = 3
            case 10:
                self.exp = 4

    def draw(self):
        self.games_played += 1

    def reset(self):
        self.exp = 0
        self.consecutive_games = 0
        self.games_played = 0
        self.points = 0

    def __str__(self):
        return "Nickname: {}, Level: {}, Color: {}, Wins {}".format(self.nickName, self.exp, self._col, self.consecutive_games)