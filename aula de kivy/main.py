from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 

class Box(BoxLayout):
    pass

class MainApp(App):
    def build(self):
        return Box()

MainApp().run()