import pandas as pd
import PySimpleGUI as sg

def janela_1():
    layout = [
        [sg.Push(), sg.Text('Login'), sg.Push()],
        [sg.Push(), sg.Button('Garçom 1',size=(15,2)), sg.Push(),sg.Button('Garçom 2',size=(15,2)), sg.Push()],
        [sg.Push(), sg.Button('Garçom 3',size=(15,2)), sg.Push(),sg.Button('Garçom 4',size=(15,2)), sg.Push()]
    ]
    return sg.Window('Comanda', layout=layout, finalize=True)

def janela_2():
    layout = [
        [sg.Push(), sg.Text(f'{user}'), sg.Push()],
        [],
        [],
        [sg.Push(), sg.Text('Senha:'), sg.Push()],
        [sg.Push(),sg.Input(k='senha', do_not_clear=False),sg.Push()],
        [sg.Push(),sg.Button('Login'),sg.Push()]
        
    ]
    return sg.Window('Comanda', layout=layout, finalize=True)

def janela_3():
    layout = [
        [sg.Push(), sg.Text(f'CONSEGUI PORRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'), sg.Push()],
        
        
    ]
    return sg.Window('Comanda', layout=layout, finalize=True)

#Planilha com os cadastro de login e senha
    
login = pd.read_excel('missaocertificacaoaulas\planilhas\comanda online\login.xlsx')
print(login)


janela1 = janela_1()
janela2 = None

while True:
    
    janela,evento,valor = sg.read_all_windows()
    
    if evento == sg.WIN_CLOSED:
        janela.close()
        break
    if evento == 'Garçom 1':
        user = evento
        janela2=janela_2()
        janela1.hide()
    if evento == 'Garçom 2':
        user = evento
        janela2=janela_2()
        janela1.hide()
    if evento == 'Garçom 3':
        user = evento
        janela2=janela_2()
        janela1.hide()
    if evento == 'Garçom 4':
        user = evento
        janela2=janela_2()
        janela1.hide()
    if evento == 'Login':
        s = valor['senha']
        if s == '':
            #sg.popup('Digite uma senha válida!')
            senha = 0
        else:
            senha = int(s)
        
        c = 0
        while True: 
            cont = c
            autent = login.loc[cont]
            aut_user = autent[0]
            aut_senha = autent[1]
            print('-='*12)
            print(cont)
            print('-='*12)
            if user == aut_user:
                if senha == aut_senha:
                    sg.popup('Logado com sucesso')
                    janela2.hide()
                    janela3=janela_3()
                    break
                else:
                    sg.popup('Senha invalida')
                    break  
            else:
                c += 1
            
        
        
        ''''''
        
        
        
        
        
        '''print('-='*12)
        print(f'Contador: {cont}')
        print('-='*12)
        print(autent)
        print('-='*12)'''
        
        '''print(c, aut_user, aut_senha)
        print('-='*12)
        print(c, user, senha)
        print('-='*12)'''
    
                
        
                    
            

            
            
            