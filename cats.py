import pygame

class Cat(pygame.sprite.Sprite):
	'''Класс каждого блока'''
	def __init__(self, screen, x, y, animList):
		super(Cat,self).__init__()
		self.screen = screen
		self.animList = animList
		self.anima = 1
		self.cat_active = 0
		self.image = self.animList[self.cat_active][0]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.timer = False

	def draw(self):
		self.screen.blit( self.animList[self.cat_active-1][self.anima], self.rect)

	def update(self, active_cat):
		self.cat_active = active_cat
		if self.timer: # Когда таймер запущен
			if self.anima < 23:
				self.anima += 1
			else:
				self.anima = 1
		else:
			self.anima = 1

class CatCard(pygame.sprite.Sprite):
	'''Класс каждого блока'''
	def __init__(self, screen, x, y, card):
		super(CatCard,self).__init__()
		self.screen = screen
		# Info
		self.img_active = pygame.image.load(card['active']).convert_alpha()
		self.img_no_buy = pygame.image.load(card['no_buy']).convert_alpha()
		self.img_buy = pygame.image.load(card['buy']).convert_alpha()
		self.count = int(card['count'])
		self.name = card['name']
		self.status = card['status']

		self.image = self.img_no_buy
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def draw(self):
		self.screen.blit( self.image, self.rect)
		
	def update(self):
		if self.status == "buy":
			self.image = self.img_buy

		elif self.status == "active":
			self.image = self.img_active

		elif self.status == "no_buy":
			self.image = self.img_no_buy