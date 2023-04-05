from tkinter import *

def imprimir():
    ve=esporte.get()
    if ve == 'f':
        print('Esporte: Futebol')
    elif ve == 'v':
        print('Esporte: Vôlei')
    elif ve == 'b':
        print('Esporte: Basquete')
    else:
        print('Selecione um esporte!')

app=Tk()
app.title('Estudos')
app.geometry('500x300')

lista_esportes=['Futebol','Volêi','Basquete']

esporte=StringVar()
esporte.set(lista_esportes[0]) #definir valor padrão

bl_esportes=Label(app,text='Esportes')
bl_esportes.pack()

op_esportes=OptionMenu(app,esporte,*lista_esportes )


btn_esporte=Button(app,text='Esporte selecionado',command=imprimir)
btn_esporte.pack()

app.mainloop()