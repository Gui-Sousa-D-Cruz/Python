from tkinter import*

app=Tk()

app.title('Aula 2')
app. geometry('768x600')
app.configure(background='#7BA8D4')


Label(app,text=f'Nome:',bg='#7BA8D4',fg='#000',anchor=W).place(x=10,y=10,width=100,height=20)
vnome=Entry(app)
vnome.place(x=10,y=30,width=200,height=20)

Label(app,text=f'Telefone:',bg='#7BA8D4',fg='#000',anchor=W).place(x=10,y=60,width=100,height=20)
vfone=Entry(app)
vfone.place(x=10,y=80,width=200,height=20)

Label(app,text=f'E-mail:',bg='#7BA8D4',fg='#000',anchor=W).place(x=10,y=110,width=100,height=20)
vmail=Entry(app)
vmail.place(x=10,y=130,width=200,height=20)

Label(app,text=f'Observações:',bg='#7BA8D4',fg='#000',anchor=W).place(x=10,y=160,width=100,height=20)
vobs=Text(app)
vobs.place(x=10,y=180,width=300,height=80)

app.mainloop()