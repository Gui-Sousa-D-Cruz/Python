from tkinter import *

app = Tk()
app.title('Estudos')
app.geometry('500x300')
app.configure(bg='#dde')

lb1= Label(app, text='Nome:',bg='#dde',fg='#009',anchor=W)
lb1.place(x=10,y=10,width=100,height=20)

inp1=Entry(app) 
#metodo que permite digitar e armazenar um texto de linha simples
inp1.place(x=10,y=30,width=200,height=20)

lb2= Label(app, text='Telefone:',bg='#dde',fg='#009',anchor=W)
lb2.place(x=10,y=60,width=100,height=20)
inp2=Entry(app) 
inp2.place(x=10,y=80,width=200,height=20)

lb3= Label(app, text='E-mail:',bg='#dde',fg='#009',anchor=W)
lb3.place(x=10,y=110,width=100,height=20)
inp3=Entry(app)
inp3.place(x=10,y=130,width=200,height=20)

lb3= Label(app, text='Observações:',bg='#dde',fg='#009',anchor=W)
lb3.place(x=10,y=160,width=100,height=20)
inp3=Text(app) 
#metodo que permite digitar texto de varias linhas
inp3.place(x=10,y=180,width=300,height=80)



app.mainloop()