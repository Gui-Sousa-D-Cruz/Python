# importação da biblioteca
from tkinter import *
import os

import mysql.connector


# Armazena o diretório do arquivo
c = os.path.dirname(os.path.abspath(__file__))
dados = c + '\\dados.txt'



# Função para imprimir os dados
def impdados():
    arquivo = open(dados, 'a')
    arquivo.write('Nome: %s' % tb_nome.get())
    arquivo.write('\nTelefone: %s' % tb_tel.get())
    arquivo.write('\nEmail: %s' % tb_mail.get())
    arquivo.write('\nOBS: %s' % tb_obs.get(1.0, END))
    arquivo.write('\n\n')
    arquivo.write('----------------')
    arquivo.close()

    print('Dados Gravados!')

# Função pra salvar os dados no banco de dados
def salvar():
    #armazena os dados preenchidos no formulário (Entry)
    pnome = '%s' % tb_nome.get()
    ptel = '%s' % tb_tel.get()
    pmail = '%s' % tb_mail.get()
    pobs = '%s' % tb_obs.get(1.0, END)
    pid = int('%s' % tb_id.get())
    #Comando para inserir dados na tabela
    comando = f"INSERT INTO dados (id,nome,telefone,email,obs) VALUES ('{pid}','{pnome}','{ptel}','{pmail}','{pobs}')"
    cursor.execute(comando)
    con.commit()
    #Comando para limpar o formulário (Entry)
    tb_nome.delete(0, END)
    tb_tel.delete(0, END)
    tb_mail.delete(0, END)
    tb_obs.delete(1.0, END)

def consultar():
    comando1=f"SELECT * FROM dados"
    cursor.execute(comando1)
    res = cursor.fetchall()
    print(res)




#Váriavel para armarzenar os dados da conexão com o BD
con = mysql.connector.connect(
    host='localhost',
    database='cadastro',
    user='root',
    password=''
)
#Teste para verificar se o programa se conectou com o BD
if con.is_connected():
    dbInfo = con.get_server_info()
    print(f'Conectado ao servidor MySQL {dbInfo}')
    cursor = con.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print(f'Conectado ao banco de dados {linha}')

# Variavel para criar a tela
app = Tk()

# Define o nome da janela
app.title('Tutorial de Interface gráfica')

# Define o tamanho da janela
app.geometry('500x300')

# Define as configurações da janela
app.configure(background='#5F2599')

# variavel para gerenciar o componente
lb1 = Label(app, text='Nome', background='#B870FF', foreground='#000000', anchor=W)

# método para posicionar o componente
lb1.place(x=10, y=10, width=100, height=20)
tb_nome = Entry(app)
tb_nome.place(x=10, y=30, width=200, height=20)

lb2 = Label(app, text='Telefone', background='#B870FF', foreground='#000000', anchor=W)
lb2.place(x=10, y=50, width=100, height=20)
tb_tel = Entry(app)
tb_tel.place(x=10, y=70, width=200, height=20)

lb3 = Label(app, text='E-mail', background='#B870FF', foreground='#000000', anchor=W)
lb3.place(x=10, y=90, width=100, height=20)
tb_mail = Entry(app)
tb_mail.place(x=10, y=110, width=200, height=20)

lb4 = Label(app, text='OBS:', background='#B870FF', foreground='#000000', anchor=W)
lb4.place(x=10, y=130, width=100, height=20)
tb_obs = Text(app)
tb_obs.place(x=10, y=150, width=200, height=80)

lb5 = Label(app, text='ID', background='#B870FF', foreground='#000000', anchor=W)
lb5.place(x=230, y=10, width=100, height=20)
tb_id = Entry(app)
tb_id.place(x=230, y=30, width=200, height=20)



#lb6 = Label(app, text='Consulta', background='#B870FF', foreground='#000000', anchor=W)
#lb6.place(x=230, y=50, width=100, height=20)
#lb7 = Label(app, text=f'{amostra}', background='#FFFFFF', foreground='#000000', anchor=W)
#lb7.place(x=230, y=70, width=250, height=110)

#btn2 = Button(app, text='Consultar', command = consultar)
#btn2.place(x=230, y=200, width=100, height=20)

btn1 = Button(app, text='Enviar', command = salvar)
btn1.place(x=10, y=250, width=100, height=20)





app.mainloop()

if con.is_connected():
    cursor.close()
    con.close()
    print('Conexão ao MySQL foi encerrada ')