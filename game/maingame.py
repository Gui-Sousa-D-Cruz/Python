from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

act = 0

class tela(BoxLayout):
    pass

class Game(App):
    def build(self):
        return tela()
        
   

Game().run()


