import unittest
import gameAI

class testGame(unittest.TestCase):
	def setUP(self):
		self.heli1 = copter(0, 0)
		self.heli2 = copter(500, 600)
		self.heli3 = copter(250, 300)

	def test_jump(self):
		self.heli1.jump()
		self.assertEual(self.heli1.velocity, -10)
		self.assertEual(self.heli1.tick_cnt, 0)

		self.heli2.jump()
		self.assertEual(self.heli2.velocity, -10)
		self.assertEual(self.heli2.tick_cnt, 0)

	def test_move(self):
		pass
