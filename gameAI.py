import pygame
import neat
import time
import os
import random

WIDTH = 600
HEIGHT = 800

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game AI")


class copter:
	"""docstring for copter"""
	def __init__(self, x, y):
		''' initialize the copter object and
			sets positional param '''
		self.x, self.y = x, y
		self.velocity = 0
		self.height = self.y
		# self.img = pygame.draw.circle(screen, BLUE, pos, 20)

	def move(self):
		''' move the copter '''

run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.draw.circle(win, (255,0,0), (300, 400), 20)
	pygame.display.update()

pygame.quit()
quit()