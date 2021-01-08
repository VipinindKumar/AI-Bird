import pygame
import neat
import time
import os
import random

from collections import deque

WIDTH = 500
HEIGHT = 600
FPS = 30
ACCELERATION = 1
BACKGROUND = (25,25,25)#(105,105,105)
ROTATION = 15
THICKNESS = 20
OBSTCOLOR = (192,192,192)
SPEED = 5
GAP = 100

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
		self.velocity = 0.5
		self.tick_cnt = 0
		self.tilt = 0
		self.image = pygame.image.load("img/copter.png")

	def draw(self):
		''' draw the copter on window '''
		rotImage = pygame.transform.rotate(self.image, self.tilt)

		win.blit(rotImage, (self.x, self.y))

	def move(self):
		''' move the copter '''
		self.tick_cnt += 1

		# s = v*t + 1/2*a*t^2
		displ = (self.velocity * self.tick_cnt +
				(1/2) * (ACCELERATION) * (self.tick_cnt) ** 2)

		# stop accelerating after certain point, (kinda terminal velocity)
		if displ > 15:
			displ = 15

		# add tilt to the copter
		# tilt up if going up
		if displ < 0:
			self.tilt = ROTATION
		# else just point down
		else:
			self.tilt = -ROTATION

		# update the position of the copter
		self.y += displ

	def jump(self):
		''' make the bird jump'''
		self.velocity = -4
		self.tick_cnt = 0

	def mask(self):
		'''returns the mask for the bird'''
		return pygame.mask.from_surface(self.image)

class obstacle(object):
	"""docstring for obstacle"""
	def __init__(self,x, y):
		self.x, self.y = x, y
		self.width = random.randrange(100, 500)
		
	def draw(self):
		'''draws the obstacle rectangle
		at x,y with defined thickness and width'''
		self.image = pygame.Rect(self.x, self.y, self.width, THICKNESS)
		pygame.draw.rect(win, OBSTCOLOR, self.image)

	def move(self):
		'''move obstacle left by speed'''
		self.x -= SPEED

	def passedEnd(self):
		'''fn to tell if end of the screen has been passed'''
		if (self.x + self.width) < WIDTH:
			return True
		return False

	def collision(self, copter):
		'''returns True if obstacle and 
		copter are overlapping'''
		cRect = copter.image.get_rect()
		cRect.topleft = (copter.x, copter.y)
		
		return cRect.colliderect(self.image)

		# print(copterMask)
		# # obstacleMask = pygame.mask.from_surface(self.image)
		# pygame.sprite.collide_mask
		# # rect to surface
		# pygame.Surface((a.w, a.h))


copter1 = copter(WIDTH / 4, HEIGHT / 2)
obstrn = deque()
obstrn.append(obstacle(500, 250))

run = True
while run:
	# to stop execution press 'q' on keyboard
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				run = False
			elif event.key == pygame.K_j:
				copter1.jump()

	# clear screen
	win.fill(BACKGROUND)

	copter1.move()
	for obst in obstrn:
		obst.move()
		obst.draw()
		obst.collision(copter1)

	# create new obstacle, to keep them adjacent
	if obstrn[-1].passedEnd():
		# code to get obstcles with a certain gap b/w them
		# cordY = obstrn[-1].y
		# rdm = random.randrange(100, cordY)
		# if rdm > (cordY - GAP):
		# 	rdm += (2 * GAP)

		# ineffiecient implementation for getting gap
		cordY = obstrn[-1].y
		rdm = cordY
		while rdm > (cordY-GAP) and rdm < (cordY+GAP):
			rdm = random.randrange(100, 500)

		obstrn.append(obstacle(500, rdm))

	copter1.draw()
	pygame.display.update()
	fpsClock.tick(FPS)

pygame.quit()
quit()