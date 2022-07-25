from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class adder(BoxLayout):
    pass

class Test4(App):
    def build(self):
        return adder()
        


Test4().run()