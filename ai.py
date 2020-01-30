class ai:
    def __init__(self, board, current_index):
        self.game_board = board
        self.current_index = current_index
        self.suggested_move = 0

    def updateBoard(self, board):
        self.game_board = board

    def updateCurrentIndex(self, current_index):
        self.current_index = current_index

    def imminentLoss(self):
        return True

    def possibleWinningMove(self):
        return True

    def possibleOffensiveMove(self):
        return True

    def possibleDefensiveMove(self):
        return True
