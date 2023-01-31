'''
	CatTracker v2.0
'''

# 	IMPORT
import json
import time


#	KIVY
from kivy.config import Config
#Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 360)
Config.set('graphics', 'height', 640)

from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.core.text import Label as CoreLabel
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

from kivy.clock import Clock


Window.title = "Cat Tracker"
Window.clearcolor = (255/255, 233/255, 189/255)

class TimerScreen(Screen):
	def __init__(self, **kwargs):
		super(TimerScreen,self).__init__(**kwargs)

		# Variable
		# Timer
		self.count = 0
		self.timer_ctrl = False

		# Anim Box Result
		self.anim_box_ctrl = False

		# Settings
		self.ids.cat__image._coreimage.anim_reset(True)
		self.ids.cat__image.anim_delay = -1
		
	def Callback_Clock(self, dt):
		self.count = self.count + 1
		new_time = str( time.strftime("%M:%S", time.gmtime(self.count)) )
		self.ids.clock__text.text = new_time

	def Animate_box_result(self, dt):
		box_pos_x = self.ids.result__box.pos[0]
		box_pos_y = self.ids.result__box.pos[1]

		if box_pos_y != self.center_y - self.ids.result__box.height // 2:
			box_pos_y += 5

			self.ids.result__box.pos = (box_pos_x,box_pos_y)
		else:
			self.anim_box.cancel()
			return

	def get_timer(self):
		if self.timer_ctrl:
			# Stop
			self.timer.cancel()
			self.ids.clock__text.text = "00:00"
			
			print(self.count)
			if self.count < 30:
				# Game Over
				self.timer_ctrl = False
				self.ids.cat__image.anim_delay = -1
				self.ids.cat__image.anim_loop = 0
				self.count = 0

			else:
				# VIN
				self.timer_ctrl = False
				self.ids.cat__image.anim_delay = -1
				self.ids.cat__image.anim_loop = 0
				self.count = 0
				self.anim_box = Clock.schedule_interval(self.Animate_box_result, 0.01)
				self.anim_box_ctrl = True
			
		else:
			# Start
			self.timer = Clock.schedule_interval(self.Callback_Clock, 1)
			self.timer_ctrl = True
			
			self.ids.cat__image.anim_delay = 0.1
			self.ids.cat__image.anim_loop = 0

			if self.anim_box_ctrl:

				self.ids.result__box.pos = (self.center_x - self.ids.result__box.width // 2,0 -)
				self.anim_box_ctrl = False


class ShopScreen(Screen):
	def __init__(self, **kwargs):
		super(ShopScreen,self).__init__(**kwargs)


class CatTrackerApp(App):
	def __init__(self, **kwargs):
		super(CatTrackerApp,self).__init__(**kwargs)
		self.load_kv("main.kv")

	def build(self):
		self.sm = ScreenManager(transition=NoTransition())

		self.sm.add_widget(TimerScreen(name="timer"))
		self.sm.add_widget(ShopScreen(name="shop"))
		self.sm.current = 'timer'
		return self.sm


if __name__ == '__main__':
	CatTrackerApp().run()