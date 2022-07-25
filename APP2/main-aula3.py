import re
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from time import sleep

class Test(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text='Botão 1', font_size=30,on_release=self.release)
        self.label = Label(text='0',font_size=30)
        box.add_widget(button)
        box.add_widget(self.label)
        return box
    def release (self,button):
        button.text='Soltei'
        self.label.text = str(int(self.label.text)+1)
    
        


Test().run()