from tkinter import *
import customtkinter


app = customtkinter.CTk()
app.title('Game')
app.geometry('768x600')
app.configure(background='#93A9EB')

'''
vtxt = 'Curso de Python'
vbg = '#AC8FF6'
vfg = '#000'


txt1=Label(app,text=vtxt,bg=vbg,fg=vfg)
txt1.place(x=309,y=0,width=150,height=30,fill=X,expand=True)

'''

vtxt = 'Curso de Python2'
vbg = '#000'
vfg = '#AC8FF6'

txt2=Label(app,text=vtxt,bg=vbg,fg=vfg)
txt2.pack(ipadx=20,ipady=20,side='top',fill=X,expand=True)

app.mainloop() 