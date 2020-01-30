from gomoku.ai import ai

class gomoku:
    def __init__(self):
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
        self.game_board = []
        for x in range(15):
            for y in range(15):
                self.game_board.append(".")

    def getBoard(self):
        return self.game_board

    def getMoveIndex(self, x, y):
        return (y * 15) + x

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
                    # 96 will stop the loop after looping through 4 times while incrementing by 16. (16 * 5 = 80)
                    (self.doesNotCrossRows(x, 16, 80, 16))):
                self.setBold(x, 2)
                return True
        # Left diagonal test
        # Goes to row 10(rows start at 0 and go to 14) and column O(15) so no index errors occur
        for x in range(165):
            if ((self.game_board[x] ==
                 self.game_board[x + 14] ==
                 self.game_board[x + 14 * 2] ==
                 self.game_board[x + 14 * 3] ==
                 self.game_board[x + 14 * 4] ==
                 player) and
                    (self.doesNotCrossRows(x, 14, 70, 14))):
                self.setBold(x, 3)
                return True
        return False

    def setBold(self, x, win_type):
        if win_type == 0:
            self.game_board[x] = f"\033[09m{self.game_board[x]}\033[00m"
            self.game_board[x + 15] = f"\033[09m{self.game_board[x + 15]}\033[00m"
            self.game_board[x + 15 * 2] = f"\033[09m{self.game_board[x + 15 * 2]}\033[00m"
            self.game_board[x + 15 * 3] = f"\033[09m{self.game_board[x + 15 * 3]}\033[00m"
            self.game_board[x + 15 * 4] = f"\033[09m{self.game_board[x + 15 * 4]}\033[00m"
        elif win_type == 1:
            self.game_board[x] = f"\033[09m{self.game_board[x]}\033[00m"
            self.game_board[x + 1] = f"\033[09m{self.game_board[x + 1]}\033[00m"
            self.game_board[x + 2] = f"\033[09m{self.game_board[x + 2]}\033[00m"
            self.game_board[x + 3] = f"\033[09m{self.game_board[x + 3]}\033[00m"
            self.game_board[x + 4] = f"\033[09m{self.game_board[x + 4]}\033[00m"
        elif win_type == 2:
            self.game_board[x] = f"\033[09m{self.game_board[x]}\033[00m"
            self.game_board[x + 16] = f"\033[09m{self.game_board[x + 16]}\033[00m"
            self.game_board[x + 16 * 2] = f"\033[09m{self.game_board[x + 16 * 2]}\033[00m"
            self.game_board[x + 16 * 3] = f"\033[09m{self.game_board[x + 16 * 3]}\033[00m"
            self.game_board[x + 16 * 4] = f"\033[09m{self.game_board[x + 16 * 4]}\033[00m"
        elif win_type == 3:
            self.game_board[x] = f"\033[09m{self.game_board[x]}\033[00m"
            self.game_board[x + 14] = f"\033[09m{self.game_board[x + 14]}\033[00m"
            self.game_board[x + 14 * 2] = f"\033[09m{self.game_board[x + 14 * 2]}\033[00m"
            self.game_board[x + 14 * 3] = f"\033[09m{self.game_board[x + 14 * 3]}\033[00m"
            self.game_board[x + 14 * 4] = f"\033[09m{self.game_board[x + 14 * 4]}\033[00m"

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

    def makeAIMove(self, player, i):
        if self.game_board[i] == ".":
            self.game_board[i] = player
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

def playAI():
    b = gomoku()
    current_index = 0
    a = ai(b.getBoard(), current_index)
    players = ["\033[91mX\033[00m", "\033[94m0\033[00m"]
    turn = 0
    while not b.gameOver():
        print(b)
        # Player's turn
        if turn == 0:
            moves: list
            move: str = input(f"Player {players[turn]}, what is your move?\n")
            move = move.lstrip()
            move = move.rstrip()
            try:
                moves = move.split(" ")
                moves[1] = moves[1].upper()
                moves[1] = b.letters.index(moves[1])
                if b.makeMove(players[turn], int(moves[1]), int(moves[0])):
                    turn = not turn
                    current_index = b.getMoveIndex(int(moves[1]), int(moves[0]))
            except ValueError:
                print(
                    f"\033[91mGiven invalid position {move}, position must be integer between 0 and 14 inclusive and a "
                    f"letter between A and P inclusive separated by a space\033[00m")
            except IndexError:
                print(
                    f"\033[91mGiven invalid position {move}, position must be integer between 0 and 14 inclusive and a "
                    f"letter between A and P inclusive separated by a space\033[00m")
        # AI's turn
        elif turn == 1:
            a.updateBoard(b.getBoard())
            a.updateCurrentIndex(current_index)
            if a.possibleWinningMove():
                b.makeAIMove(players[turn], a.suggested_move)
                turn = not turn
            elif a.imminentLoss():
                b.makeAIMove(players[turn], a.suggested_move)
                turn = not turn
            elif a.possibleOffensiveMove():
                b.makeAIMove(players[turn], a.suggested_move)
                turn = not turn
            elif a.possibleDefensiveMove():
                b.makeAIMove(players[turn], a.suggested_move)
                turn = not turn
    print(b)
    print("Game Over\n")
    if b.hasWon(f"\033[09m{players[0]}\033[00m"):
        print(f"Player {players[0]} has won!")
    elif b.hasWon(f"\033[09m{players[1]}\033[00m"):
        print(f"The AI has won!")
    else:
        print("Its a tie!")


def playGomoku():
    b = gomoku()
    players = ["\033[91mX\033[00m", "\033[94m0\033[00m"]
    turn = 0
    while not b.gameOver():
        print(b)
        moves: list
        move: str = input(f"Player {players[turn]}, what is your move?\n")
        move = move.lstrip()
        move = move.rstrip()
        try:
            moves = move.split(" ")
            moves[1] = moves[1].upper()
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
    if b.hasWon(f"\033[09m{players[0]}\033[00m"):
        print(f"Player {players[0]} has won!")
    elif b.hasWon(f"\033[09m{players[1]}\033[00m"):
        print(f"Player {players[1]} has won!")
    else:
        print("Its a tie!")


if __name__ == '__main__':
    print(f"\033[01mWelcome to a python 3.8 implementation of Gomoku\033[00m"
          f"\n\033[04mRules\033[00m:"
          f"\n1. The first player to place 5 pieces in a row horizontally, vertically, or diagonally wins the game."
          f"\n2. A move is made by typing a number between 0 and 14 to choose a row and a letter between A and O to "
          f"choose a column. The number and letter should be separate by a space."
          f"\n3. Any game session can be ended by typing 'terminate' into the terminal."
          f"\n4. Type any letter and press enter to begin playing")
    buffer: str = input()
    playAgain = True
    while playAgain:
        playGomoku()
        ask: str = input(f"\n\033[01m"
                         f"wish to play again? (y or n)"
                         f"\033[00m\n")
        ask.lower()
        if ask != "y":
            playAgain = False
