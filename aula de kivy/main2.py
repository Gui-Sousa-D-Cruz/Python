from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 

class Box(BoxLayout):
    pass

class Main2App(App):
    def build(self):
        return Box()

Main2App().run()