import json
import time

import pygame
from cats import CatCard
from Toast import Toast

scene_tracker = 0
scene_shop = 1

#	SETTINGS
WIDTH = 360
HEIGHT = 640
FPS = 20 # Колличество фреймов для анимации

def update_count(screen, font, count):
	text = font.render(str(count), True, (255,255,255))
	text_rect = text.get_rect()
	text_rect.center = (320,25)
	screen.blit(text, text_rect)

def Activity(pygame, screen, config):
	pygame.font.init()
	clock = pygame.time.Clock()
	font = pygame.font.SysFont('Ubuntu', 20)

	# User
	active_cat = config['user']["active_cat"]
	scin = config['user']["scin"]
	count = int(config['user']["count"])

	#	OBJECTS
	item1 = CatCard(screen, 29, 70, config['card'][0])
	item2 = CatCard(screen, 199, 70, config['card'][1])
	item3 = CatCard(screen, 29, 267, config['card'][2])
	toast = Toast(screen, 28, 155, font, "Привет :-)", "assets/TOAST.png")

	#	LOOP
	while True:
		clock.tick(FPS)
		screen.fill((255, 199, 150))
		screen.blit(pygame.image.load('assets/back_shop.png'), (0,0))

		#	DRAWING
		screen.blit(pygame.image.load('assets/cookies.png'), (246,8))
		item1.draw()
		item2.draw()
		item3.draw()
		toast.draw()


		#	EVENTS
		for event in pygame.event.get():
			if event.type == pygame.QUIT:

				config['user']["active_cat"] = active_cat
				config['user']["scin"] = scin
				config['user']["count"] = count
				config['card'][0]["status"] = item1.status
				config['card'][1]["status"] = item2.status
				config['card'][2]["status"] = item3.status

				with open('config.json', 'w') as file_config:
					json.dump(config, file_config)
				
				time.sleep(3)
				pygame.quit()

			elif event.type == pygame.KEYDOWN: # Кнопка назад
				if event.key == pygame.K_ESCAPE:

					config['user']["active_cat"] = active_cat
					config['user']["scin"] = scin
					config['user']["count"] = count
					config['card'][0]["status"] = item1.status
					config['card'][1]["status"] = item2.status
					config['card'][2]["status"] = item3.status

					with open('config.json', 'w') as file_config:
						json.dump(config, file_config)

					return scene_tracker, config

			if event.type == pygame.MOUSEBUTTONDOWN: # Обработка кликов
				if event.button == 1:
					OnClick_mouse_pos = pygame.mouse.get_pos()

					# Item 1
					if OnClick_mouse_pos[0] >= item1.rect.x and OnClick_mouse_pos[0] <= item1.rect.x + 136:
						if OnClick_mouse_pos[1] >= item1.rect.y and OnClick_mouse_pos[1] <= item1.rect.y + 154:
							# Проверка на наличие 
							if item1.status == "active": # Если куплен и выбран
								toast.text = "У Вас уже есть данный кот"
								toast.active = True

							if item1.status == "no_buy": # Если не куплен
								if int(item1.count) <= int(count):
									count -= item1.count
									item1.status = "active"
									if item2.status == "active":
										item2.status = "buy"
									if item3.status == "active":
										item3.status = "buy"
									active_cat = "1"

									toast.text = "Вы купили этого кота!"
									toast.active = True
								else:
									toast.text = "Не достаточно средств!"
									toast.active = True

							if item1.status == "buy": # Если куплен, но не выбран
								item1.status = "active"
								if item2.status == "active":
									item2.status = "buy"
								if item3.status == "active":
									item3.status = "buy"
								active_cat = "1"

					# Item 2
					if OnClick_mouse_pos[0] >= item2.rect.x and OnClick_mouse_pos[0] <= item2.rect.x + 136:
						if OnClick_mouse_pos[1] >= item2.rect.y and OnClick_mouse_pos[1] <= item2.rect.y + 154:
							# Проверка на наличие 
							if item2.status == "active": # Если куплен и выбран
								toast.text = "У Вас уже есть данный кот"
								toast.active = True

							if item2.status == "no_buy": # Если не куплен
								if int(item2.count) <= int(count):
									count -= item2.count
									item2.status = "active"
									if item1.status == "active":
										item1.status = "buy"
									if item3.status == "active":
										item3.status = "buy"
									active_cat = "2"

									toast.text = "Вы купили этого кота!"
									toast.active = True
								else:
									toast.text = "Не достаточно средств!"
									toast.active = True

							if item2.status == "buy": # Если куплен, но не выбран
								item2.status = "active"
								if item3.status == "active":
									item3.status = "buy"
								if item1.status == "active":
									item1.status = "buy"
								active_cat = "2"

					# Item 3
					if OnClick_mouse_pos[0] >= item3.rect.x and OnClick_mouse_pos[0] <= item3.rect.x + 136:
						if OnClick_mouse_pos[1] >= item3.rect.y and OnClick_mouse_pos[1] <= item3.rect.y + 154:
							# Проверка на наличие 
							if item3.status == "active": # Если куплен и выбран
								toast.text = "У Вас уже есть данный кот"
								toast.active = True

							if item3.status == "no_buy": # Если не куплен
								if int(item3.count) <= int(count):
									count -= item3.count
									item3.status = "active"
									if item2.status == "active":
										item2.status = "buy"
									if item1.status == "active":
										item1.status = "buy"
									active_cat = "3"

									toast.text = "Вы купили этого кота!"
									toast.active = True
								else:
									toast.text = "Не достаточно средств!"
									toast.active = True

							if item3.status == "buy": # Если куплен, но не выбран
								item3.status = "active"
								if item2.status == "active":
									item2.status = "buy"
								if item1.status == "active":
									item1.status = "buy"
								active_cat = "3"
		#	UPDATES	
		item1.update()
		item2.update()
		item3.update()
		toast.update()
		update_count(screen, font, count)
		pygame.display.flip()