'''
	Мур Мяу кодировка v2.0
	Графическое окружение
'''

''' 
	COLORS:
		(0/255, 0/255, 0/255, 1) - Background
		(63/255, 63/255, 63/255, 1) - Ponel

		(135/255, 194/255, 133/255, 1) - Green
		(153/255, 219/255, 150/255, 1) - Duble Green

		(219/255, 74/255, 74/255, 1) - Red

		(79/255, 56/255, 146/255, 1) - Purple
		(108/255, 73/255, 211/255, 1) - Duble Purple
		(183/255, 162/255, 245/255, 1) - TextInput Purple
'''
# 	IMPORT
import json

#	KIVY
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 840)
Config.set('graphics', 'height', 640)

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty, StringProperty

Window.title = "Every Day"
Window.clearcolor = (0/255, 0/255, 0/255)

# Управление базой данных
class Base():
	def __init__(self,**kwargs):
		super(Base,self).__init__(**kwargs)

		with open('base.json', 'r') as file_base:
			self.connect = json.load(file_base)

	def save(self):
		# Сохранение базы данных
		with open('base.json', 'w') as file_base:
			json.dump(self.connect, file_base)

	def add_new_today_task(self, text, key, status=True):
		self.connect['task']['today'].append({
			'text':str(text),
			"status":"not_finished",
			"key":str(key)})
		self.save()


class PlansScreen(Screen):
	def __init__(self,**kwargs):
		super(PlansScreen,self).__init__(**kwargs)
		self.base = Base()

		self.ctrl_add_tast = 0
		self.ids.input_add_task.opacity = 0
		self.ids.add_input_title_task.opacity = 0
		self.ids.add_input_keys_task.opacity = 0
		self.ids.add_input_button_task.opacity = 0
		self.ids.input_add_task.size = (0,0)
		self.ids.add_input_title_task.size = (0,0)
		self.ids.add_input_keys_task.size = (0,0)
		self.ids.add_input_button_task.size = (0,0)

		self.task_list = []
		if len(self.base.connect['task']['today']) != 0:
			for item_task in range( len(self.base.connect['task']['today']) ):
				self.task_list.append(
					self.base.connect['task']['today'][item_task]
					)
		self.ids.rv.data = self.task_list
		
	def add_new_task(self):
		if self.ctrl_add_tast == 0:
			self.ids.add_task.text = "Отмена"
			self.ids.add_task.background_color = (219/255, 74/255, 74/255)
			
			self.ids.input_add_task.opacity = 1
			self.ids.add_input_title_task.opacity = 1
			self.ids.add_input_keys_task.opacity = 1
			self.ids.add_input_button_task.opacity = 1
			
			self.ids.input_add_task.size = (395,175)
			self.ids.add_input_title_task.size = (375,75)
			self.ids.add_input_keys_task.size = (375,35)
			self.ids.add_input_button_task.size = (375,35)

			self.ctrl_add_tast = 1

		elif self.ctrl_add_tast == 1:
			self.ids.add_task.text = "Добавить"
			self.ids.add_task.background_color = (135/255, 194/255, 133/255)
			
			self.ids.input_add_task.opacity = 0
			self.ids.add_input_title_task.opacity = 0
			self.ids.add_input_keys_task.opacity = 0
			self.ids.add_input_button_task.opacity = 0
			
			self.ids.input_add_task.size = (0,0)
			self.ids.add_input_title_task.size = (0,0)
			self.ids.add_input_keys_task.size = (0,0)
			self.ids.add_input_button_task.size = (0,0)

			self.ctrl_add_tast = 0

	def add_input_task(self):
		title = self.ids.add_input_title_task.text
		keys = self.ids.add_input_keys_task.text

		self.ids.rv.data.append( {'text':title} )
		self.base.add_new_today_task(title, keys)

		self.ids.add_input_title_task.text = ""
		self.ids.add_input_keys_task.text = ""

		self.ids.add_task.text = "Добавить"
		self.ids.add_task.background_color = (135/255, 194/255, 133/255)
		self.ids.input_add_task.opacity = 0
		self.ids.input_add_task.size = (0,0)


class MyButtonInListView(Button):

	def callback(self,instance):
		ps = PlansScreen()
		
		ps.task_list = []
		for item_task in range( len(ps.base.connect['task']['today']) ):
			if instance == ps.base.connect['task']['today'][item_task]['text']:
				ps.base.connect['task']['today'][item_task]['status'] = True
				ps.base.save()


class TodayScreen(Screen):
	def __init__(self, **kwargs):
		super(TodayScreen,self).__init__(**kwargs)
		self.base = Base()

		self.num_kl_today = 0
		self.num_kl_plan = 0
		self.procent_plan_and_today = str((self.num_kl_plan // 100) * self.num_kl_today) + "%"

		self.ids.procent_in_circule.text = self.procent_plan_and_today
		self.ids.today_in_circule.text = "0kl"
		self.ids.plan_in_circule.text = "0kl"

		if len(self.base.connect['task']['today']) != 0:
			self.ids.list_item_1.text = self.base.connect['task']['today'][0]['text']
			if len(self.base.connect['task']['today']) != 1:
				self.ids.list_item_2.text = self.base.connect['task']['today'][1]['text']
				if len(self.base.connect['task']['today']) != 2:
					self.ids.list_item_3.text = self.base.connect['task']['today'][2]['text']


class EveryDayApp(App):
	def __init__(self, **kwargs):
		super(EveryDayApp,self).__init__(**kwargs)
		self.load_kv("main.kv")

	def build(self):
		self.sm = ScreenManager(transition=NoTransition())

		self.sm.add_widget(TodayScreen(name="today"))
		self.sm.add_widget(PlansScreen(name="plans"))

		return self.sm


if __name__ == '__main__':
	EveryDayApp().run()