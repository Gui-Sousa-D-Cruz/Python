from tkinter import *
import os

pastaApp=os.path.dirname(__file__)

def semComando():
    print('')

def novoContato():
    exec(open(pastaApp+'\\aula060.py').read(),{'x':10})

app = Tk()
app.title('Estudos')
app.geometry('500x300')
app.configure(bg='#dde')

menus = Menu(app)
menuCont = Menu(menus,tearoff=0) 
menuCont.add_command(label='Novo',command=novoContato)
menuCont.add_command(label='Excluir',command=semComando)
menuCont.add_command(label='Pesquisar',command=semComando)
menus.add_cascade(label='Contatos',menu=menuCont)

menuMan = Menu(menus,tearoff=0)
menuMan.add_command(label='Banco de Dados', command=semComando)
menus.add_cascade(label='Manutenção',menu=menuMan)

menuSob = Menu(menus,tearoff=0)
menuSob.add_command(label='Gui',command=semComando)
menus.add_cascade(label='Sobre',menu=menuSob)

app.config(menu=menus)

app.mainloop()

