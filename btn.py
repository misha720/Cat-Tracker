import pygame

class Start(pygame.sprite.Sprite):
	'''Класс каждого блока'''
	def __init__(self, screen, x, y):
		super(Start,self).__init__()
		self.screen = screen
		self.image = pygame.image.load('assets/START.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.timer = False

	def draw(self):
		self.screen.blit( self.image, self.rect)

	def update(self):
		if self.timer:
			self.image = pygame.image.load('assets/STOP.png').convert_alpha()
		else:
			self.image = pygame.image.load('assets/START.png').convert_alpha()

class Shop(pygame.sprite.Sprite):
	'''Класс каждого блока'''
	def __init__(self, screen, x, y):
		super(Shop,self).__init__()
		self.screen = screen
		self.image = pygame.image.load('assets/shop.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def draw(self):
		self.screen.blit( self.image, self.rect)