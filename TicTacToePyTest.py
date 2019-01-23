
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


if __name__ == '__main__':
	unittest.main()