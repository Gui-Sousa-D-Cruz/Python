from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import keyboard

class tela(BoxLayout):
    pass

class Game(App):
    def build(self):
        return tela()
        
   

Game().run()