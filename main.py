import json

import pygame
import TrackerActivity as Tracker
import ShopActivity as Shop
# import layout__game as Game

pygame.init()
scene_tracker = 0
scene_shop = 1

WIDTH = 360
HEIGHT = 640

def engine():
	screen = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption('Cats Tracker')
	activity = scene_tracker# В начале запустить
	with open('config.json', 'r') as file_config:
		config = json.load(file_config)

	while True:
		if activity == scene_tracker:
			activity, config = Tracker.Activity(pygame, screen, config)
		elif activity == scene_shop:
			activity, config = Shop.Activity(pygame, screen, config)

#	Run
if __name__ == '__main__':
	engine()