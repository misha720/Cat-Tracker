import pygame

class Toast(pygame.sprite.Sprite):
	'''Класс каждого блока'''
	def __init__(self, screen, x, y, font, text, image):
		super(Toast,self).__init__()
		self.screen = screen
		self.image = pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.WIDTH = 360
		self.HEIGHT = 640
		self.text = text
		self.font = font
		self.active = False # True если тост выводится
		self.deley = 0 # Задержка в секундах

	def draw(self):
		if self.active:
			self.screen.blit( self.image, self.rect)

			text = self.font.render(self.text, True, (255,255,255))
			text_rect = text.get_rect()
			text_rect.center = (self.WIDTH // 2, self.HEIGHT // 2)

			self.screen.blit(text, text_rect)

	def update(self):
		if self.active: # Когда таймер запущен
			if self.deley < 100:
				self.deley += 1
			else:
				self.deley = 0
				self.active = False
		else:
			self.deley = 0