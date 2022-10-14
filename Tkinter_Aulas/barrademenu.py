from tkinter import *
import os

def semComando():
    print('')

app = Tk()
app.title('Teste de Barra de menu')
app.geometry('500x300')
app.configure(background='#dde')

#Cria o widget de barra de Menus
barraMenus=Menu(app)
#Cria um menu
menuCont=Menu(barraMenus,tearoff=0)
#Cria os componentes da barra de menu
menuCont.add_command(label="Novo",command=semComando)
menuCont.add_command(label="Abrir",command=semComando)
menuCont.add_command(label="Excluir",command=semComando)
menuCont.add_separator()
menuCont.add_command(label="Fechar",command=app.quit)
#Adiciona a aba do menu
barraMenus.add_cascade(label='Contatos',menu=menuCont)
#Adiciona o menu no app
app.config(menu=barraMenus)



app.mainloop()