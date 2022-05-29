import imp
from kivy.app import App 
from kivy.lang import Builder
import requests

GUI = Builder.load_file('tela.kv')

class Game(App):
    def build(self):
        return GUI
    def on_start(self):
        self.root.ids['f1'].text = 'Teste 1'
        self.root.ids['f2'].text = 'Teste 2'
       

Game().run()