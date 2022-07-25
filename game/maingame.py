import re
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Test(App):
    def build(self):
        
    
        box = BoxLayout(orientation='vertical')
        box0 = BoxLayout()
        label1 = Label(text='')
        label2 = Label(text='')
        box0.add_widget(label1)
        box0.add_widget(label2)

        box.add_widget(box0)
        label = Label(text='Ao adentrar a pirâmide, você nota diversos hierógrifos na parede, o que deseja fazer?')
        box.add_widget(label)

        box0 = BoxLayout()
        label1 = Label(text='')
        label2 = Label(text='')
        box0.add_widget(label1)
        box0.add_widget(label2)

        box.add_widget(box0)
        
        box2 = BoxLayout()
        button1 = Button(text='Investigar.')
        button2 = Button(text='Passar direto.')
        box2.add_widget(button1)
        box2.add_widget(button2)

        box.add_widget(box2)

        box3 = BoxLayout()
        button3 = Button(text='Inventário.')
        button4 = Button(text='Fugir.')
        box3.add_widget(button3)
        box3.add_widget(button4)

        box.add_widget(box3)

        
        return box


Test().run()