
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
		if self.board[0] != '-' and self.board[0] == self.board[1] and self.board[1] == self.board[2]:
			return self.board[0]
		if self.board[3] != '-' and self.board[3] == self.board[4] and self.board[4] == self.board[5]:
			return self.board[3]
		if self.board[6] != '-' and self.board[6] == self.board[7] and self.board[7] == self.board[8]:
			return self.board[6]
		return '-'
