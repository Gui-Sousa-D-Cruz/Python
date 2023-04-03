from tkinter import *

app = Tk() #importa a classe TK para uma variavel
app.title('ESTUDOS') #metodo para o titulo da janela
app.geometry('500x300')#metodo para o tamanho da janela
app.configure(background='#008')#metodo que configura a janela

txt1=Label(app,text='Curso de Python',bg='#008' , fg='#fff') #cria um widget do tipo label
txt1.place(x=10,y=10,width=150,height=30) 
# metodo que posiciona o label criado

vtxt2='Módulo Tkinter'
vbg='#ff0'
vfg='#000'

txt2=Label(app,text=vtxt2, bg=vbg, fg=vfg)
txt2.pack(ipadx=20,ipady=20,padx=5,pady=5,side='top',fill=Y,expand=True)#metodo posiciona o widget no container


app.mainloop() 
#roda o loop principal do app. abrindo a janela 


