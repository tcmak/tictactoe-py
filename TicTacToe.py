
class TicTacToe:

	board =""

	def __init__(self, s, pos=-1, player='-'):
		sList = list(s)
		if pos >= 0: sList[pos] = player
		self.board = "".join(sList)

	def move(self, player):
		for i in range(9):
			if self.board[i] == '-':
				game = self.play(i, player)
				if game.winner() == player:
					return i

		for i in range(9):
			if self.board[i] == '-':
				return i

		return -1

	def play(self, i, player):
		return TicTacToe(self.board, i, player)

	def winner(self):
		return '-'
