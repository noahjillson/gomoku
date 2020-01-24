class gomoku:
    def __init__(self):
        self.letters = ["A", "B", "C", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
        self.game_board = []
        for x in range(15):
            for y in range(15):
                self.game_board.append(".")

    def hasWon(self, player):
        # goes to row 10(rows start at 0 and go to 14) and column P(15) so no out of bounds errors occur
        for x in range(165):
            if (self.game_board[x] ==
                    self.game_board[x + 15] ==
                    self.game_board[x + 15 * 2] ==
                    self.game_board[x + 15 * 3] ==
                    self.game_board[x + 15 * 4] ==
                    player):
                return True
        # goes to row 14 column L(11)
        for x in range(220):
            if (self.game_board[x] ==
                    self.game_board[x + 1] ==
                    self.game_board[x + 2] ==
                    self.game_board[x + 2] ==
                    self.game_board[x + 4] ==
                    player) and (doesNotCrossRows(x)):
                return True
        return False

    def doesNotCrossRows(self, x):
        for a in range(1, 5):
            if (x + a) % 15 == 0:
                return False
        return True


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
