from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class adder(BoxLayout):
    def __init__(self,tarefas,**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa,font_size=30))
        

class Test5(App):
    def build(self):
        return adder(['Fazer compras','Jogar','Estudar'],orientation = 'horizontal')
        


Test5().run()