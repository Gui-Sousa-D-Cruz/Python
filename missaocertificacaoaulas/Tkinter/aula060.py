import mysql.connector
from tkinter import *

con = mysql.connector.connect(
    host='localhost',
    database='cadastro',
    user='root',
    password=''
)

if con.is_connected():
    dbInfo = con.get_server_info()
    print(f'Conectado ao servidor MySQL {dbInfo}')
    cursor = con.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print(f'Conectado ao banco de dados {linha}')
    
    

def salvar():
    nome = str(inp1.get())
    telefone = str(inp2.get())
    email = str(inp3.get())
    obs = str(inp4.get('1.0', END))
    print(nome, telefone, email, obs)
    comando = f'INSERT INTO dados (nome,telefone,email,obs) VALUES ("{nome}","{telefone}","{email}","{obs}")'
    cursor.execute(comando)
    con.commit()
    print('Dados adicionados com sucesso!')
    inp1.delete(0, END)
    inp2.delete(0, END)
    inp3.delete(0, END)
    inp4.delete('1.0', END)

def consultar():
    comando = 'SELECT * FROM dados'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    lista = int(len(resultado[0]))
    visual =['Id: ','Nome: ', 'Número: ', 'Email: ', 'Observação: ']
    c = 0
    cl = 0
    while True:
        while True:
            if c < lista and cl < len(resultado):
                print(f'{visual[c]}{resultado[cl][c]}')
                c += 1
            else:
                print('')
                c = 0
                break
                
        if cl < len(resultado):
            cl += 1
        else:
            break
     

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

btn1=Button(app, text='Salvar', command=salvar)
btn1.place(x=10,y=270,width=100,height=20)

btn2=Button(app, text='Consultar', command=consultar)
btn2.place(x=130,y=270,width=100,height=20)


app.mainloop()

if con.is_connected():
    cursor.close()
    con.close()
    print('Conexão ao MySQL foi encerrada ')