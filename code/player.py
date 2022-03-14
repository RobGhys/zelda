import pygame 
from settings import *

class Player(pygame.sprite.Sprite):

	"""
	Constructor
	position: the position of the tile
	groups: the groups to which the tile belongs
	"""
	def __init__(self, position, groups, obstacle_sprites):

		# Init the pygame.sprite.Sprite super class
		super().__init__(groups)

		self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
		# Give a position to the tile
		self.rect = self.image.get_rect(topleft = position)

		self.direction = pygame.math.Vector2()
		self.speed = 5
		self.obstacle_sprites = obstacle_sprites

	def input(self):
		keys = pygame.key.get_pressed()

		# y
		if keys[pygame.K_UP]:
			self.direction.y = -1
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
		else:
			self.direction.y = 0

		# x
		if keys[pygame.K_LEFT]:
			self.direction.x = -1
		elif keys[pygame.K_RIGHT]:
			self.direction.x = 1
		else:
			self.direction.x = 0

	def move(self, speed):
		# magnitude is the length of the vector
		if self.direction.magnitude() != 0:
			# set direction to 1 to normalize the speed
			self.direction = self.direction.normalize()

		# x movement
		self.rect.x += self.direction.x * speed
		self.collision('horizontal')
		# y movement
		self.rect.y += self.direction.y * speed
		self.collision('vertical')

	def collision(self, direction):
		if direction == 'horizontal':
			# check for collisions
			for sprite in self.obstacle_sprites:
				if sprite.rect.colliderect(self.rect):
					if self.direction.x > 0: # player is moving right
						# Move right side to the player to the left of the obstacle
						self.rect.right = sprite.rect.left
					if self.direction.x < 0:
						# Flip side
						self.rect.left = sprite.rect.right

		if direction == 'vertical':
			if sprite.rect.colliderect(self.rect):
				if self.direction.y > 0:  # player is moving down
					self.rect.bottom = sprite.rect.top
				if self.direction.y < 0: # player is moving up
					# Flip side
					self.rect.top = sprite.rect.bottom

	def update(self):
		self.input()
		self.move(self.speed)