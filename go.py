class gomoku:
    def __init__(self):
        self.letters = ["A", "B", "C", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
        self.game_board = []
        for x in range(15):
            for y in range(15):
                self.game_board.append(".")

    def hasWon(self, player):
        for x in range(149):
            if (self.game_board[x] ==
                    self.game_board[x + 15] ==
                    self.game_board[x + 15 * 2] ==
                    self.game_board[x + 15 * 3] ==
                    self.game_board[x + 15 * 4] ==
                    player):
                return True
            if (self.game_board[x] ==
                    self.game_board[x + 1] ==
                    self.game_board[x + 2] ==
                    self.game_board[x + 2] ==
                    self.game_board[x + 4] ==
                    player) and () :
                return True
        return False

    def __str__(self):
        string = "    "
        i = -1
        for x in range(15):
            string += self.letters[x]
            string += "  "
        for x in self.game_board:
            i += 1
            if i % 15 == 0:
                string += "\n"
                string += str(i // 15)
                if i // 15 > 9:
                    string += "  "
                else:
                    string += "   "
                string += x
                string += "  "
            else:
                string += x
                string += "  "

        return string


if __name__ == '__main__':
    b = gomoku()
    print(b)
