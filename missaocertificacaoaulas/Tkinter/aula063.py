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

esporte=StringVar()
cor=StringVar()

bl_esportes=Label(app,text='Esportes')
bl_esportes.pack()

rb_futebol=Radiobutton(app,text='Futebol',value='f',variable=esporte)
rb_futebol.pack()

rb_volei=Radiobutton(app,text='Vôlei',value='v',variable=esporte)
rb_volei.pack()

rb_basquete=Radiobutton(app,text='Basquete',value='b',variable=esporte)
rb_basquete.pack()


rb_verde=Radiobutton(app,text='Verde',value='#0f0',variable=cor)
rb_verde.pack()

rb_vermelho=Radiobutton(app,text='Vermelho',value='$f00',variable=cor)
rb_vermelho.pack()




btn_esporte=Button(app,text='Esporte selecionado',command=imprimir)
btn_esporte.pack()

app.mainloop()