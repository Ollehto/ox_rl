import numpy as np

class OXGame():
	def __init__(self, board=np.zeros((3, 3), dtype=np.int8), player_first=True):
		self.__board = board
		self.__player_first = player_first
		self.__player = 1 if player_first else -1

		if not player_first:
			self.computer_set()

	def __repr__(self):
		return str(self.__board)

	def __decide_win(self):
		for p in (1, -1):
			board = self.__board == p
			if np.any(np.all(board, axis=1)) or np.any(np.all(board, axis=0)):
				return p
			elif np.all(board[(0, 1, 2), (0, 1, 2)]) or np.all(board[(2, 1, 0), (0, 1, 2)]):
				return p
		return 0

	def __computer_set(self):
		flatind = np.random.choice(np.where(self.__board.ravel() == 0)[0])# get indices of cells where no o/x is placed
		self.__board.ravel()[flatind] = -1 * self.__player
		return self.__decide_win()

	def __player_set(self, place):
		self.__board[place] = self.__player
		return self.__decide_win()

	def set(self, place):
		if self.__player_first:
			win = self.__player_set(place)
			if win != 0:
				return win
			cp_win = self.__computer_set()
			return cp_win
		else:
			cp_win = self.__computer_set()
			if cp_win != 0:
				return cp_win
			win = self.__player_set(place)
			return win

class Agent:
	def __init__(self):
		pass

if __name__ == '__main__':
	ox = OXGame(board=np.array([[0, 1, 1], [0, 0, 0], [0, 0, 0]]))
	print(ox.set((2, 0)))
	print(ox)