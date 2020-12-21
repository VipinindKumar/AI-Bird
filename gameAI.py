import pygame
import neat
import time
import os
import random

WIDTH = 500
HEIGHT = 600
FPS = 30

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game AI")
fpsClock = pygame.time.Clock()

class copter:
	"""docstring for copter"""
	def __init__(self, x, y):
		''' initialize the copter object and
			sets positional param '''
		self.x, self.y = x, y
		self.velocity = 1

	def draw(self):
		''' draw the copter on window '''

		myimage = pygame.image.load("img/copter.png")

		win.blit(myimage, (self.x, self.y))

	def move(self):
		''' move the copter '''
		


copter1 = copter(WIDTH / 4, HEIGHT / 2)

run = True
while run:
	# to stop execution press 'q' on keyboard
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				run = False

	copter1.draw()
	pygame.display.update()
	fpsClock.tick(FPS)

pygame.quit()
quit()