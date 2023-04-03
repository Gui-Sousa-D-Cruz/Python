from tkinter import *
import os

c = os.path.dirname(__file__) #pega o diretorio do arquivo
bd = f'{c}\\nomes.txt'


def salvar():
    arquivo=open(bd,'a') #abre o arquivo e anexa
    arquivo.write('Nome....: %s' % inp1.get()) #escreve no arquivo
    arquivo.write('\nTelefone: %s' % inp2.get())
    arquivo.write('\nEmail...: %s' % inp3.get())
    arquivo.write('\nOBS.....: %s' % inp4.get('1.0', END))
    arquivo.write('\n')
    arquivo.close()
    print('Nome....: %s' % inp1.get())
    print('Telefone: %s' % inp2.get())
    print('Email...: %s' % inp3.get())
    print('OBS.....: %s' % inp4.get('1.0', END))

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

lb4= Label(app, text='Observações:',bg='#dde',fg='#009',anchor=W)
lb4.place(x=10,y=160,width=100,height=20)
inp4=Text(app) 
#metodo que permite digitar texto de varias linhas
inp4.place(x=10,y=180,width=300,height=80)

btn1=Button(app, text='Imprimir', command=salvar)
btn1.place(x=10,y=270,width=100,height=20)


app.mainloop()