import mysql.connector

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


#CRUD
'''dbnome = ''
dbtel = ''
dbemail =''
dbobs =''
comando = "INSERT INTO dados (nome,telefone,email,obs) VALUES ()"
cursor.execute(comando)
con.commit() # edita o banco de dados'''


#Teste para verificar se a conexão foi encerrada
if con.is_connected():
    cursor.close()
    con.close()
    print('Conexão ao MySQL foi encerrada ')