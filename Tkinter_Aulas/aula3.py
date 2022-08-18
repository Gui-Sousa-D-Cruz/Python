from tkinter import*
import os 



c = os.path.dirname(__file__)
nomeArquivo=c+'\\nomes.txt'



def gravarDados():
    arquivo=open(nomeArquivo,'a')
    arquivo.write('Nome: %s' % vnome.get())
    arquivo.write('\nTelefone: %s' % vfone.get())
    arquivo.write('\nEmail: %s' % vmail.get())
    arquivo.write('\nOBS: %s' % vobs.get(1.0, END))
    arquivo.write('\n\n')
    arquivo.close()


   
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

btn=Button(app,text='Gravar',command=gravarDados)
btn.place(x=10,y=270,width=100,height=20)



app.mainloop()