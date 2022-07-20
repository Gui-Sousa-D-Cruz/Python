#importar o app
#importar o builder (GUI)
#Criar o app
#Criar a função build 
from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file('tela.kv')

class Comanda(App):
    def build(self):
        return GUI