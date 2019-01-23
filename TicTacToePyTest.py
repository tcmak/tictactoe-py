
from TicTacToe import TicTacToe
import unittest

class TicTacToeTest(unittest.TestCase):

	def test_only_available_move(self):
		game = TicTacToe("XOXOX-OXO")
		assert game.move('X') == 5

		game = TicTacToe("XOXOXOOX-")
		assert game.move('O') == 8

	def test_starting_default_move(self):
		game = TicTacToe("---------")
		assert game.move('X') == 0

	def test_no_available_move(self):
		game = TicTacToe("XXXXXXXXX")
		assert game.move('X') == -1

	def test_find_winning_row_move(self):
		game = TicTacToe("OO-XX-OOX")
		assert game.move('X') == 5

	def test_win_by_row_conditions(self):
		game = TicTacToe("---XXX---")
		assert game.winner() == 'X'

		game = TicTacToe("------OOO")
		assert game.winner() == 'O'

if __name__ == '__main__':
	unittest.main()
