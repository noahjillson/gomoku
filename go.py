class gomoku:
    def __init__(self):
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
        self.game_board = []
        for x in range(15):
            for y in range(15):
                self.game_board.append(".")

    def hasWon(self, player):
        # Vertical test
        # Goes to row 10(rows start at 0 and go to 14) and column O(15) so no out of bounds errors occur
        for x in range(165):
            if (self.game_board[x] ==
                    self.game_board[x + 15] ==
                    self.game_board[x + 15 * 2] ==
                    self.game_board[x + 15 * 3] ==
                    self.game_board[x + 15 * 4] ==
                    player):
                self.setBold(x, 0)
                return True
        # Horizontal test
        # Goes to row 14 column K(11)
        for x in range(220):
            if ((self.game_board[x] ==
                 self.game_board[x + 1] ==
                 self.game_board[x + 2] ==
                 self.game_board[x + 2] ==
                 self.game_board[x + 4] ==
                 player)
                    and
                    (self.doesNotCrossRows(x, 1, 5, 1))):
                self.setBold(x, 1)
                return True
        # Right diagonal test
        # Goes to row 10(rows start at 0 and go to 14) and column K(11) so no index errors occur
        for x in range(161):
            if ((self.game_board[x] ==
                 self.game_board[x + 16] ==
                 self.game_board[x + 16 * 2] ==
                 self.game_board[x + 16 * 3] ==
                 self.game_board[x + 16 * 4] ==
                 player)
                    and
                    # 96 will stop the loop after looping through 4 times while incrementing by 16. (16 * 5 = 96)
                    (self.doesNotCrossRows(x, 16, 96, 16))):
                return True
        return False

    def setBold(self, x, win_type):
        if win_type == 0:
            self.game_board[x] = f"\033[09m{self.game_board[x]}\033[00m"
            self.game_board[x + 15] = f"\033[09m{self.game_board[x + 15]}\033[00m"
            self.game_board[x + 15 * 2] = f"\033[09m{self.game_board[x + 15 * 2]}\033[00m"
            self.game_board[x + 15 * 3] = f"\033[09m{self.game_board[x + 15 * 3]}\033[00m"
            self.game_board[x + 15 * 4] = f"\033[09m{self.game_board[x + 15 * 4]}\033[00m"

        if win_type == 1:
            self.game_board[x] = f"\033[09m{self.game_board[x]}\033[00m"
            self.game_board[x + 1] = f"\033[09m{self.game_board[x + 1]}\033[00m"
            self.game_board[x + 2] = f"\033[09m{self.game_board[x + 2]}\033[00m"
            self.game_board[x + 3] = f"\033[09m{self.game_board[x + 3]}\033[00m"
            self.game_board[x + 4] = f"\033[09m{self.game_board[x + 4]}\033[00m"

    def doesNotCrossRows(self, x, start, stop, step) -> bool:
        for a in range(start, stop, step):
            if (x + a) % 15 == 0:
                return False
        return True

    def makeMove(self, player, x, y):
        if self.game_board[(y * 15) + x] == ".":
            self.game_board[(y * 15) + x] = player
            return True
        return False

    def gameOver(self):
        if self.hasWon("\033[91mX\033[00m") or self.hasWon("\033[94mO\033[00m"):
            return True
        elif "." in self.game_board:
            return False
        return True

    def clearBoard(self):
        for x in range(len(self.game_board)):
            self.game_board[x] = "."

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


def playGomoku():
    b = gomoku()
    players = ["\033[91mX\033[00m", "\033[94m0\033[00m"]
    turn = 0
    while not b.gameOver():
        print(b)
        moves: list
        move: str = input(f"Player {players[turn]}, what is your move?\n")
        move.lstrip()
        move.rstrip()
        try:
            moves = move.split(" ")
            moves[1] = b.letters.index(moves[1])
            if b.makeMove(players[turn], int(moves[1]), int(moves[0])):
                turn = not turn
        except ValueError:
            print(f"\033[91mGiven invalid position {move}, position must be integer between 0 and 14 inclusive and a "
                  f"letter between A and P inclusive separated by a space\033[00m")
        except IndexError:
            print(f"\033[91mGiven invalid position {move}, position must be integer between 0 and 14 inclusive and a "
                  f"letter between A and P inclusive separated by a space\033[00m")
    print(b)
    print("Game Over\n")
    if b.hasWon(players[0]):
        print(f"Player {players[0]} has won!")
    elif b.hasWon(players[1]):
        print(f"Player {players[1]} has won!")
    else:
        print("Its a tie!")


if __name__ == '__main__':
    playGomoku()