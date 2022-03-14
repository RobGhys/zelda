import pygame 
from settings import *

class Player(pygame.sprite.Sprite):

	"""
	Constructor
	position: the position of the tile
	groups: the groups to which the tile belongs
	"""
	def __init__(self, position, groups):

		# Init the pygame.sprite.Sprite super class
		super().__init__(groups)

		self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
		# Give a position to the tile
		self.rect = self.image.get_rect(topleft = position)