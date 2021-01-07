import unittest

class testGame(unittest.TestCase):
	def setUP(self):
		self.heli1 = copter(0, 0)
		self.heli2 = copter(500, 600)
		self.heli3 = copter(250, 300)

