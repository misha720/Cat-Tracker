import json
import time

import pygame
from cats import Cat
from btn import Start, Shop

scene_tracker = 0
scene_shop = 1

#	SETTINGS
WIDTH = 360
HEIGHT = 640
FPS = 20 # Колличество фреймов для анимации

def update_clock(screen, font, zero_time, now_time):
	timer_sec = now_time // 1000 - zero_time // 1000
	text = font.render(str( time.strftime("%M:%S", time.gmtime(timer_sec)) ), True, (255,255,255))
	text_rect = text.get_rect()
	text_rect.center = (WIDTH // 2,480)
	screen.blit(text, text_rect)

def Activity(pygame, screen, config):
	pygame.font.init()
	clock = pygame.time.Clock()
	font = pygame.font.SysFont('Ubuntu', 50)

	timer_active = False # Работает ли таймер
	zero_time = 0

	animCats = [
		[pygame.image.load('assets/cat1_activity/1.png').convert_alpha(),
	pygame.image.load('assets/cat1_activity/1.png').convert_alpha(),

	pygame.image.load('assets/cat1_activity/2.png').convert_alpha(),
	pygame.image.load('assets/cat1_activity/2.png').convert_alpha(),

	pygame.image.load('assets/cat1_activity/3.png').convert_alpha(),
	pygame.image.load('assets/cat1_activity/3.png').convert_alpha(),

	pygame.image.load('assets/cat1_activity/4.png').convert_alpha(),
	pygame.image.load('assets/cat1_activity/4.png').convert_alpha(),

	pygame.image.load('assets/cat1_activity/5.png').convert_alpha(),
	pygame.image.load('assets/cat1_activity/5.png').convert_alpha(),

	pygame.image.load('assets/cat1_activity/6.png').convert_alpha(),
	pygame.image.load('assets/cat1_activity/6.png').convert_alpha(),

	pygame.image.load('assets/cat1_activity/7.png').convert_alpha(),
	pygame.image.load('assets/cat1_activity/7.png').convert_alpha(),

	pygame.image.load('assets/cat1_activity/8.png').convert_alpha(),
	pygame.image.load('assets/cat1_activity/8.png').convert_alpha(),

	pygame.image.load('assets/cat1_activity/9.png').convert_alpha(),
	pygame.image.load('assets/cat1_activity/9.png').convert_alpha(),

	pygame.image.load('assets/cat1_activity/10.png').convert_alpha(),
	pygame.image.load('assets/cat1_activity/10.png').convert_alpha(), 

	pygame.image.load('assets/cat1_activity/11.png').convert_alpha(),
	pygame.image.load('assets/cat1_activity/11.png').convert_alpha(),

	pygame.image.load('assets/cat1_activity/12.png').convert_alpha(),
	pygame.image.load('assets/cat1_activity/12.png').convert_alpha(),],
		[pygame.image.load('assets/cat2_activity/1.png').convert_alpha(),
		pygame.image.load('assets/cat2_activity/1.png').convert_alpha(),

		pygame.image.load('assets/cat2_activity/2.png').convert_alpha(),
		pygame.image.load('assets/cat2_activity/2.png').convert_alpha(),

		pygame.image.load('assets/cat2_activity/3.png').convert_alpha(),
		pygame.image.load('assets/cat2_activity/3.png').convert_alpha(),

		pygame.image.load('assets/cat2_activity/4.png').convert_alpha(),
		pygame.image.load('assets/cat2_activity/4.png').convert_alpha(),

		pygame.image.load('assets/cat2_activity/5.png').convert_alpha(),
		pygame.image.load('assets/cat2_activity/5.png').convert_alpha(),

		pygame.image.load('assets/cat2_activity/6.png').convert_alpha(),
		pygame.image.load('assets/cat2_activity/6.png').convert_alpha(),

		pygame.image.load('assets/cat2_activity/7.png').convert_alpha(),
		pygame.image.load('assets/cat2_activity/7.png').convert_alpha(),

		pygame.image.load('assets/cat2_activity/8.png').convert_alpha(),
		pygame.image.load('assets/cat2_activity/8.png').convert_alpha(),

		pygame.image.load('assets/cat2_activity/9.png').convert_alpha(),
		pygame.image.load('assets/cat2_activity/9.png').convert_alpha(),

		pygame.image.load('assets/cat2_activity/10.png').convert_alpha(),
		pygame.image.load('assets/cat2_activity/10.png').convert_alpha(), 

		pygame.image.load('assets/cat2_activity/11.png').convert_alpha(),
		pygame.image.load('assets/cat2_activity/11.png').convert_alpha(),

		pygame.image.load('assets/cat2_activity/12.png').convert_alpha(),
		pygame.image.load('assets/cat2_activity/12.png').convert_alpha(),],
		[pygame.image.load('assets/cat3_activity/1.png').convert_alpha(),
	pygame.image.load('assets/cat3_activity/1.png').convert_alpha(),

	pygame.image.load('assets/cat3_activity/2.png').convert_alpha(),
	pygame.image.load('assets/cat3_activity/2.png').convert_alpha(),

	pygame.image.load('assets/cat3_activity/3.png').convert_alpha(),
	pygame.image.load('assets/cat3_activity/3.png').convert_alpha(),

	pygame.image.load('assets/cat3_activity/4.png').convert_alpha(),
	pygame.image.load('assets/cat3_activity/4.png').convert_alpha(),

	pygame.image.load('assets/cat3_activity/5.png').convert_alpha(),
	pygame.image.load('assets/cat3_activity/5.png').convert_alpha(),

	pygame.image.load('assets/cat3_activity/6.png').convert_alpha(),
	pygame.image.load('assets/cat3_activity/6.png').convert_alpha(),

	pygame.image.load('assets/cat3_activity/7.png').convert_alpha(),
	pygame.image.load('assets/cat3_activity/7.png').convert_alpha(),

	pygame.image.load('assets/cat3_activity/8.png').convert_alpha(),
	pygame.image.load('assets/cat3_activity/8.png').convert_alpha(),

	pygame.image.load('assets/cat3_activity/9.png').convert_alpha(),
	pygame.image.load('assets/cat3_activity/9.png').convert_alpha(),

	pygame.image.load('assets/cat3_activity/10.png').convert_alpha(),
	pygame.image.load('assets/cat3_activity/10.png').convert_alpha(), 

	pygame.image.load('assets/cat3_activity/11.png').convert_alpha(),
	pygame.image.load('assets/cat3_activity/11.png').convert_alpha(),

	pygame.image.load('assets/cat3_activity/12.png').convert_alpha(),
	pygame.image.load('assets/cat3_activity/12.png').convert_alpha(),]
	]

	# OBJ
	cat = Cat(screen, 49, 124, animCats)
	btn_start = Start(screen, 105, 540)
	btn_shop = Shop(screen, 302, 12)

	#	LOOP
	while True:
		clock.tick(FPS)
		screen.fill((255, 199, 150))
		screen.blit(pygame.image.load('assets/back_main.png'), (0,0))
		
		# User
		active_cat = config['user']["active_cat"]
		scin = config['user']["scin"]
		count = int(config['user']["count"])

		#	DRAWING
		cat.draw()
		btn_start.draw()
		btn_shop.draw()
		if timer_active:
			update_clock(screen, font, zero_time, pygame.time.get_ticks())

		#	EVENTS
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					OnClick_mouse_pos = pygame.mouse.get_pos()

					# Нажатие на СТАРТ или СТОП
					if OnClick_mouse_pos[0] >= btn_start.rect.x and OnClick_mouse_pos[0] <= btn_start.rect.x + 158:
						if OnClick_mouse_pos[1] >= btn_start.rect.y and OnClick_mouse_pos[1] <= btn_start.rect.y + 58:
							if timer_active == False: # Запуск таймера
								btn_start.timer = True
								cat.timer = True

								timer_active = True
								zero_time = pygame.time.get_ticks()
								update_clock(screen, font, zero_time, pygame.time.get_ticks())

							else: # Остановка Таймера
								btn_start.timer = False
								cat.timer = False
								timer_active = False

					# Нажатие на МАГАЗИН
					if OnClick_mouse_pos[0] >= btn_shop.rect.x and OnClick_mouse_pos[0] <= btn_shop.rect.x + 45:
						if OnClick_mouse_pos[1] >= btn_shop.rect.y and OnClick_mouse_pos[1] <= btn_shop.rect.y + 45:
							return scene_shop, config
		
		#	UPDATES
		cat.update(int(active_cat))
		btn_start.update()
		btn_shop.update()
		pygame.display.flip()